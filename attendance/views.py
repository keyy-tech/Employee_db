from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from .models import Leave
from employee.models import Employee


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
def my_leave_requests(request):
    """View to show only the leave requests of the logged-in user."""
    employee = request.user.employee
    leaves = Leave.objects.filter(employee=employee)
    return render(request, "leave/my_leave_requests.html", {"leaves": leaves})
