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


def attendance_view(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance recorded successfully.")
            return redirect("attendance")
        else:
            messages.error(
                request, "Error recording attendance. Please check the form for errors."
            )
    else:
        form = AttendanceForm()
    return render(request, "attendance/attendance.html", {"form": form})
