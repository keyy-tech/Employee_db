from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_user_and_employee, name="create_user_and_employee"),
    path(
        "update/<int:user_id>/",
        views.update_employee,
        name="update_employee",
    ),
    path(
        "delete/<int:user_id>/",
        views.delete_employee,
        name="delete_employee",
    ),
    path("list/", views.list_employees, name="employee_list"),
    path("create_department/", views.create_department, name="create_department"),
    path(
        "update_department/<int:id>/", views.update_department, name="update_department"
    ),
    path(
        "delete_department/<int:id>/", views.delete_department, name="delete_department"
    ),
    path("list_department/", views.read_departments, name="department_list"),
]
