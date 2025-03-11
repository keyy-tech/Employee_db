from django.urls import path

from . import views

urlpatterns = [
    path("request/", views.leave_request_view, name="leave_request"),  # Request leave
    path(
        "update/<int:id>/", views.update_leave_view, name="update_leave"
    ),  # Update leave
    path("delete/<int:id>/", views.delete_leave, name="delete_leave"),  # Delete leave
    path(
        "approve/<int:id>/", views.approve_leave, name="approve_leave"
    ),  # Approve leave
    path("reject/<int:id>/", views.reject_leave, name="reject_leave"),  # Reject leave
    path("view/", views.leave_list, name="leave_list"),  # View all leave requests
    path("my-leave-requests/", views.my_leave_requests, name="my_leave_requests"),
    path("check-in/", views.check_in, name="check_in"),
    path("check-out/", views.check_out, name="check_out"),
    path(
        "attendance/", views.attendance_list, name="attendance_list"
    ),  # View logged-in user's leave requests
    path(
        "approved-leave-requests/",
        views.approved_leave_requests,
        name="approved_leave_requests",
    ),
]
