from django.urls import path

from . import views

urlpatterns = [
    # Employee management URLs
    path(
        "create_employee/", views.create_employee, name="create_employee"
    ),  # Create employee
    path(
        "update/<int:user_id>/", views.update_employee, name="update_employee"
    ),  # Update employee
    path(
        "delete/<int:user_id>/", views.delete_employee, name="delete_employee"
    ),  # Delete employee
    path(
        "list_employees/", views.list_employees, name="employee_list"
    ),  # List employees
    path(
        "update_profile/", views.update_profile, name="update_profile"
    ),  # Update profile
    path("profile/", views.profile, name="profile"),  # View profile
    # Department management URLs
    path(
        "create_department/", views.create_department, name="create_department"
    ),  # Create department
    path(
        "update_department/<int:id>/", views.update_department, name="update_department"
    ),  # Update department
    path(
        "delete_department/<int:id>/", views.delete_department, name="delete_department"
    ),  # Delete department
    path(
        "list_departments/", views.read_departments, name="department_list"
    ),  # List departments
    path(
        "list_employee_department/", views.hod_employee, name="list_employee_department"
    ),
]
