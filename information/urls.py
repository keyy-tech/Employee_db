from django.urls import path

from . import views

urlpatterns = [
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/<int:id>/update/", views.update_task, name="update_task"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/my/", views.user_tasks, name="user_tasks"),  # New URL pattern for user tasks
    path("tasks/<int:task_id>/complete/", views.complete_task, name="complete_task"),  # New URL pattern for marking task as complete
    path("tasks/<int:task_id>/incomplete/", views.incomplete_task, name="incomplete_task"),  # New URL pattern for marking task as not complete
    path("announcements/", views.announcement_list, name="announcement_list"),
    path("announcements/<int:id>/", views.announcement_detail, name="announcement_detail"),
    path("announcements/create/", views.create_announcement, name="create_announcement"),
    path("announcements/<int:id>/update/", views.update_announcement, name="update_announcement"),
    path("announcements/<int:id>/delete/", views.delete_announcement, name="delete_announcement"),
]