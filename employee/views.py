from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import render, get_object_or_404, redirect

from core.forms import CustomUserForm, CustomUserUpdateForm
from core.models import CustomUser
from .forms import EmployeeForm, DepartmentForm
from .models import Employee, Department


# Role-Based Access Control (RBAC) Decorators
def hr_or_hod_required(user):
    return user.role in ["HR Manager", "HOD"]


def admin_required(user):
    return user.role == "Admin"


# HR and HOD manage employees
@login_required
@transaction.atomic
def create_employee(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            username = user_form.cleaned_data["username"]
            email = user_form.cleaned_data["email"]
            role = user_form.cleaned_data["role"]
            default_password = "default_password"
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]

            if (
                CustomUser.objects.filter(username=username).exists()
                or CustomUser.objects.filter(email=email).exists()
            ):
                messages.error(
                    request, "A user with this username or email already exists."
                )
                return render(
                    request,
                    "employee/create.html",
                    {"user_form": user_form, "employee_form": employee_form},
                )

            try:
                user = CustomUser(
                    username=username,
                    email=email,
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.set_password(default_password)
                user.save()

                employee = employee_form.save(commit=False)
                employee.user = user
                employee.save()

                messages.success(request, "Employee created successfully")
                return redirect("employee_list")
            except IntegrityError:
                messages.error(
                    request, "An error occurred while creating the employee."
                )
    else:
        user_form = CustomUserForm()
        employee_form = EmployeeForm()

    return render(
        request,
        "employee/create.html",
        {"user_form": user_form, "employee_form": employee_form},
    )


@login_required
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, "employee/list.html", {"employees": employees})


@login_required
@transaction.atomic
def update_employee(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    employee = get_object_or_404(Employee, user_id=user_id)

    if request.method == "POST":
        user_form = CustomUserUpdateForm(request.POST, instance=user)
        employee_form = EmployeeForm(request.POST, instance=employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(request, "Employee updated successfully")
            return redirect("employee_list")
    else:
        user_form = CustomUserUpdateForm(instance=user)
        employee_form = EmployeeForm(instance=employee)

    return render(
        request,
        "employee/update.html",
        {
            "user_form": user_form,
            "employee_form": employee_form,
            "user": user,
            "employee": employee,
        },
    )


@transaction.atomic
def delete_employee(request, user_id):
    employee = get_object_or_404(Employee, user_id=user_id)
    employee.user.delete()
    messages.success(request, "Employee deleted successfully")
    return redirect("employee_list")


@login_required
@transaction.atomic
def update_profile(request):
    user = request.user
    employee = get_object_or_404(Employee, user=user)

    if request.method == "POST":
        user_form = CustomUserUpdateForm(request.POST, instance=user)
        employee_form = EmployeeForm(request.POST, instance=employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(request, "Your profile was updated successfully")
            return redirect("profile")
    else:
        user_form = CustomUserUpdateForm(instance=user)
        employee_form = EmployeeForm(instance=employee)

    return render(
        request,
        "employee/update_profile.html",
        {
            "user_form": user_form,
            "employee_form": employee_form,
        },
    )


@login_required
def profile(request):
    user = request.user
    employee = get_object_or_404(Employee, user=user)
    return render(
        request, "employee/profile.html", {"user": user, "employee": employee}
    )


# HR manages departments
@login_required
def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            if Department.objects.filter(name=form.cleaned_data["name"]).exists():
                messages.error(request, "The department name is already in use.")
            else:
                form.save()
                messages.success(request, "Department created successfully")
                return redirect("department_list")
    else:
        form = DepartmentForm()
    return render(request, "department/create.html", {"form": form})


@login_required
def read_departments(request):
    departments = Department.objects.all()
    return render(request, "department/list.html", {"departments": departments})


@login_required
def update_department(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully")
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)
    return render(request, "department/update.html", {"form": form})


@login_required
def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    department.delete()
    messages.success(request, "Department deleted successfully")
    return redirect("department_list")


@login_required
def hod_employee(request):
    if request.user.role == "HOD":
        department = request.user.employee.department
        employees = Employee.objects.filter(department=department)
        context = {"employees": employees}
        return render(request, "department/employee_list.html", context)
