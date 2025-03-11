from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from employee.models import Employee
from .forms import LeaveForm, CheckInForm, CheckOutForm
from .models import Leave, Attendance


@login_required
def leave_request_view(request):
    """Allows logged-in users to request leave."""
    try:
        employee = request.user.employee  # Check if user has an Employee profile
    except Employee.DoesNotExist:
        messages.error(request, "Only employees can request leave.")
        return redirect("dashboard")  # Redirect to a generic dashboard

    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.status = "Pending"
            leave.employee = employee  # Assign the employee instance
            leave.save()
            messages.success(request, "Leave request submitted successfully.")
            return redirect("my_leave_requests")
        else:
            messages.error(
                request,
                "Error submitting leave request. Please check the form for errors.",
            )
    else:
        form = LeaveForm()
    return render(request, "leave/create.html", {"form": form})


@login_required
def update_leave_view(request, id):
    leave = get_object_or_404(Leave, id=id)

    # Check if the logged-in user is the owner of the leave request
    if leave.employee.user != request.user:
        messages.error(
            request, "You do not have permission to update this leave request."
        )
        return redirect("my_leave_requests")

    # Check if the leave request is already approved or rejected
    if leave.status in ["Approved", "Rejected"]:
        messages.error(
            request,
            "You cannot update a leave request that has been approved or rejected.",
        )
        return redirect("my_leave_requests")

    if request.method == "POST":
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave request updated successfully.")
            return redirect("my_leave_requests")
        else:
            messages.error(
                request,
                "Error updating leave request. Please check the form for errors.",
            )
    else:
        form = LeaveForm(instance=leave)
    return render(request, "leave/update.html", {"form": form, "leave": leave})


@login_required
def delete_leave(request, id):
    leave = get_object_or_404(Leave, id=id)

    # Check if the logged-in user is the owner of the leave request
    if leave.employee.user != request.user:
        messages.error(
            request, "You do not have permission to delete this leave request."
        )
        return redirect("my_leave_requests")

    # Check if the leave request is already approved or rejected
    if leave.status in ["Approved", "Rejected"]:
        messages.error(
            request,
            "You cannot delete a leave request that has been approved or rejected.",
        )
        return redirect("my_leave_requests")

    leave.delete()
    messages.success(request, "Leave request deleted successfully.")
    return redirect("my_leave_requests")


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, "leave/list.html", {"leaves": leaves})


def approve_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    if leave.status == "Rejected":
        messages.error(
            request, "Cannot approve a leave request that has already been rejected."
        )
    else:
        leave.status = "Approved"
        leave.save()
        messages.success(request, "Leave request approved successfully.")
    return redirect("leave_list")


def reject_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    if leave.status == "Approved":
        messages.error(
            request, "Cannot reject a leave request that has already been approved."
        )
    else:
        leave.status = "Rejected"
        leave.save()
        messages.success(request, "Leave request rejected successfully.")
    return redirect("leave_list")


@login_required
def approved_leave_requests(request):
    """View to show approved leave requests of employees in the HOD's department."""
    if request.user.role == "HOD":
        department = request.user.employee.department
        approved_leaves = Leave.objects.filter(
            employee__department=department, status="Approved"
        )
    else:
        approved_leaves = Leave.objects.none()  # Empty queryset for non-HOD users
    return render(
        request,
        "leave/approved_leave_requests.html",
        {"approved_leaves": approved_leaves},
    )


@login_required
def my_leave_requests(request):
    """View to show only the leave requests of the logged-in user."""
    employee = request.user.employee
    leaves = Leave.objects.filter(employee=employee)
    return render(request, "leave/my_leave_requests.html", {"leaves": leaves})


@login_required
def check_in(request):
    if request.method == "POST":
        form = CheckInForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data["employee_id"]
            try:
                employee = Employee.objects.get(id=employee_id)
            except Employee.DoesNotExist:
                messages.error(request, "Employee does not exist.")
                return redirect("check_in")

            attendance, created = Attendance.objects.get_or_create(
                employee=employee, date=timezone.now().date()
            )
            if attendance.check_in_time is None:
                attendance.check_in_time = timezone.now().time()
                attendance.save()
                messages.success(request, "Checked in successfully.")
            else:
                messages.error(request, "You have already checked in today.")
            return redirect("check_in")
    else:
        form = CheckInForm()
    return render(request, "attendance/check_in.html", {"form": form})


@login_required
def check_out(request):
    if request.method == "POST":
        form = CheckOutForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data["employee_id"]
            try:
                employee = Employee.objects.get(id=employee_id)
            except Employee.DoesNotExist:
                messages.error(request, "Employee does not exist.")
                return redirect("check_out")

            try:
                attendance = Attendance.objects.get(
                    employee=employee, date=timezone.now().date()
                )
            except Attendance.DoesNotExist:
                messages.error(request, "No check-in record found for today.")
                return redirect("check_out")

            if attendance.check_out_time is None:
                attendance.check_out_time = timezone.now().time()
                attendance.save()
                messages.success(request, "Checked out successfully.")
            else:
                messages.error(request, "You have already checked out today.")
            return redirect("check_out")
    else:
        form = CheckOutForm()
    return render(request, "attendance/check_out.html", {"form": form})


@login_required
def attendance_list(request):
    """View to display the attendance records."""
    if request.user.role == "HOD":
        department = request.user.employee.department
        attendance_records = Attendance.objects.filter(employee__department=department)
    else:
        attendance_records = Attendance.objects.all()
    return render(
        request, "attendance/list.html", {"attendance_records": attendance_records}
    )
