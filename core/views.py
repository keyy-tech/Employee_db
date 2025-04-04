from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from attendance.models import Attendance, Leave
from employee.models import Employee, Department
from information.models import Announcement
from .forms import LoginForm, CustomPasswordChangeForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")  # Redirect to the dashboard after login
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@login_required
def password_change_view(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect(
                "password_change"
            )  # Stay on password change page after success
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, "core/password_change_form.html", {"form": form})


@login_required
def dashboard_view(request):
    # Determine user role
    user_role = "Employee"  # Default role
    if request.user.is_superuser:
        user_role = "Admin"
    elif request.user.groups.filter(name="HOD").exists():
        user_role = "HOD"
    elif request.user.groups.filter(name="HR Manager").exists():
        user_role = "HR Manager"

    # Count total employees and departments
    total_employees = Employee.objects.count()
    total_departments = Department.objects.count()

    # Initialize variables
    employees_in_department = 0
    total_tasks = 0
    recent_attendance = []
    recent_leaves = []

    # Ensure request.user has an Employee object
    if hasattr(request.user, "employee") and request.user.employee:
        department = request.user.employee.department

        # Employees in department (only for HODs)
        if user_role == "HOD":
            employees_in_department = Employee.objects.filter(
                department=department
            ).count()

        # # Employee tasks (only for Employees and HODs)
        # if user_role == "Employee" or user_role == "HR Manager":
        #     total_tasks = Task.objects.filter(employee=request.user).count()

        # Recent attendance records (for department members)
        recent_attendance = Attendance.objects.filter(
            employee__department=department
        ).order_by("-check_in_time")[:5]

        # Recent leave requests (for department members)
        recent_leaves = Leave.objects.filter(employee__department=department).order_by(
            "-start_date"
        )[:5]

    # Announcements (limit to 5 most recent)
    announcements = Announcement.objects.order_by("-created_at")[:5]

    context = {
        "user_role": user_role,
        "total_employees": total_employees,
        "total_departments": total_departments,
        "employees_in_department": employees_in_department,
        "total_tasks": total_tasks,
        "announcements": announcements,
        "recent_attendance": recent_attendance,
        "recent_leaves": recent_leaves,
    }

    return render(request, "core/dashboard.html", context)


# Custom error pages
def custom_404_view(request, exception):
    return render(request, "errors/404.html", status=404)


def custom_500_view(request):
    return render(request, "errors/500.html", status=500)


def custom_403_view(request, exception):
    return render(request, "errors/403.html", status=403)


def custom_400_view(request, exception):
    return render(request, "errors/400.html", status=400)
