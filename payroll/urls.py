from django.urls import path

from . import views

urlpatterns = [
    path("", views.payroll_list, name="payroll_list"),
    path("payroll/create/<int:id>/", views.payroll_create, name="payroll_create"),
    path("update/<int:id>/", views.payroll_update, name="payroll_update"),
    path("delete/<int:id>/", views.payroll_delete, name="payroll_delete"),
]
