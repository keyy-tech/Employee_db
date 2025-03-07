from django.urls import path

from . import views

urlpatterns = [
    path("leave/create", views.leave_request_view, name="leave_request"),
    path("leave/approve/<int:id>", views.approve_leave, name="approve_leave"),
    path("leave/reject/<int:id>", views.reject_leave, name="reject_leave"),
    path("leave/update/<int:id>", views.update_leave_view, name="update_leave"),
    path("leave/delete/<int:id>", views.delete_leave, name="delete_leave"),
    path("leave/list", views.leave_list, name="leave_list"),
    path("attendance", views.attendance_view, name="attendance"),
]
