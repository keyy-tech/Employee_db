from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import LeaveForm, AttendanceForm
from .models import Leave


def leave_request_view(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.status = "Pending"
            leave.save()
            messages.success(request, "Leave request submitted successfully.")
            return redirect("leave_request")
        else:
            messages.error(
                request,
                "Error submitting leave request. Please check the form for errors.",
            )
    else:
        form = LeaveForm()
    return render(request, "leave/leave_request.html", {"form": form})


def update_leave_view(request, id):
    leave = Leave.objects.get(id=id)
    if request.method == "POST":
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave request updated successfully.")
            return redirect("leave_list")
        else:
            messages.error(
                request,
                "Error updating leave request. Please check the form for errors.",
            )
    else:
        form = LeaveForm(instance=leave)
    return render(request, "leave/leave_request.html", {"form": form, "leave": leave})


def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, "leave/leave_list.html", {"leaves": leaves})


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


def delete_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    leave.delete()
    messages.success(request, "Leave request deleted successfully.")
    return redirect("leave_list")


def attendance_create(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data["employee_id"]  # corrected from "employee"

            # Get the employee instance
            try:
                employee = Employee.objects.get(employee_id=employee_id)
            except Employee.DoesNotExist:
                messages.error(request, "This Employee ID does not exist.")
                return redirect("attendance_create")

            now = timezone.now()
            today = now.date()
            current_time = now.time()

            # Check if the employee is on leave today
            if Leave.objects.filter(
                employee=employee,
                start_date__lte=today,
                end_date__gte=today,
                status="Approved",
            ).exists():
                messages.error(
                    request, "You are currently on leave. Please contact HR."
                )
                return redirect("attendance_create")

            # Check if the employee has already checked in or out today
            attendance = Attendance.objects.filter(
                employee=employee, date=today
            ).first()
            if attendance:
                if attendance.check_out_time:
                    messages.error(request, "You have already checked out today.")
                    return redirect("attendance_create")
                else:
                    # Update check-out time
                    attendance.check_out_time = current_time
                    attendance.save()
                    messages.success(request, "Checked out successfully.")
                    return redirect("attendance_create")
            else:
                # Create a new attendance record for check-in
                attendance = Attendance(
                    employee=employee, date=today, check_in_time=current_time
                )
                attendance.save()
                messages.success(request, "Checked in successfully.")
                return redirect("attendance_create")
        else:
            messages.error(request, "Invalid form submission.")
            return redirect("attendance_create")
    else:
        form = AttendanceForm()

    return render(request, "attendance/attendance_form.html", {"form": form})
