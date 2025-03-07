from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def dashboard_view(request):
    user = request.user
    if user.role == "admin":
        return redirect("admin_dashboard")
    elif user.role == "manager":
        return redirect("manager_dashboard")
    elif user.role == "employee":
        return redirect("employee_dashboard")
    else:
        return redirect("login")


@login_required
def admin_dashboard_view(request):
    # Add context and logic specific to the admin dashboard
    return render(request, "dashboard/admin_dashboard.html")


@login_required
def manager_dashboard_view(request):
    # Add context and logic specific to the manager dashboard
    return render(request, "dashboard/manager_dashboard.html")


@login_required
def employee_dashboard_view(request):
    # Add context and logic specific to the employee dashboard
    return render(request, "dashboard/employee_dashboard.html")
