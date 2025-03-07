import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction, connection
from django.shortcuts import render, get_object_or_404, redirect

from core.forms import CustomUserForm, CustomUserUpdateForm
from core.models import CustomUser
from .forms import EmployeeForm, DepartmentForm
from .models import Employee, Department


@login_required
@transaction.atomic
def create_user_and_employee(request):
    if request.method == "POST":
        user_form = CustomUserForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            # Extract user data
            username = user_form.cleaned_data["username"]
            first_name = user_form.cleaned_data["first_name"]
            last_name = user_form.cleaned_data["last_name"]
            email = user_form.cleaned_data["email"]
            role = user_form.cleaned_data["role"]

            # Set default password
            default_password = "default_password"  # Set your default password here

            # Check for existing user
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
                # Create user instance and set password
                user = CustomUser(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role=role,
                )
                user.set_password(default_password)
                user.save()

                # Extract employee data
                phone = employee_form.cleaned_data["phone"]
                date_of_birth = employee_form.cleaned_data["date_of_birth"]
                gender = employee_form.cleaned_data["gender"]
                department = employee_form.cleaned_data["department"]
                job_position = employee_form.cleaned_data["job_position"]
                date_of_hire = employee_form.cleaned_data["date_of_hire"]
                address = employee_form.cleaned_data["address"]
                emergency_contact_name = employee_form.cleaned_data[
                    "emergency_contact_name"
                ]
                emergency_contact_phone = employee_form.cleaned_data[
                    "emergency_contact_phone"
                ]
                other_names = employee_form.cleaned_data["other_names"]

                # Generate employee_id
                unique_id = uuid.uuid4().hex[:10].upper()
                employee_id = (
                    f"{first_name[0].upper()}{last_name[0].upper()}-{unique_id}"
                )

                # Create employee instance
                employee = Employee(
                    user=user,
                    phone=phone,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    department=department,
                    job_position=job_position,
                    date_of_hire=date_of_hire,
                    employee_id=employee_id,
                    address=address,
                    emergency_contact_name=emergency_contact_name,
                    emergency_contact_phone=emergency_contact_phone,
                    other_names=other_names,
                )
                employee.save()

                messages.success(request, "Employee created successfully")
                return redirect(
                    "create_user_and_employee"
                )  # Redirect to a success page

            except IntegrityError:
                messages.error(
                    request, "An error occurred while creating the user or employee."
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
    employees = Employee.objects.select_related("user").all()
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


@login_required
@transaction.atomic
def delete_employee(request, user_id):
    if request.method == "POST":
        own_employee_id = request.POST.get("own_employee_id")
        target_employee_id = request.POST.get("target_employee_id")

        # Verify own employee ID
        own_employee = get_object_or_404(Employee, user=request.user)
        if own_employee.employee_id != own_employee_id:
            messages.error(request, "Your employee ID is incorrect.")
            return redirect("confirm_delete", user_id=user_id)

        # Verify target employee ID
        target_employee = get_object_or_404(Employee, user_id=user_id)
        if target_employee.employee_id != target_employee_id:
            messages.error(request, "The target employee ID is incorrect.")
            return redirect("confirm_delete", user_id=user_id)

        # Delete employee
        target_employee.delete()

        # Delete user
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()

        messages.success(request, "Employee deleted successfully")
        return redirect("list_employees")

    return render(request, "employee/confirm_delete.html", {"user_id": user_id})


@login_required
def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            if Department.objects.filter(name=form.cleaned_data["name"]).exists():
                messages.error(request, "The department name is already in use.")
            else:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "EXEC CreateDepartment @name=%s, @hod_id=%s",
                        [
                            form.cleaned_data["name"],
                            (
                                form.cleaned_data["hod"].id
                                if form.cleaned_data["hod"]
                                else None
                            ),
                        ],
                    )
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
    return render(
        request, "department/update.html", {"form": form, "department": department}
    )


@login_required
def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    department.delete()
    messages.success(request, "Department deleted successfully")
    return redirect("department_list")
