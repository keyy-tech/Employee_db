from django.contrib import admin
from .models import Task, Notification

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "employee", "status", "due_date", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]

class NotificationAdmin(admin.ModelAdmin):
    list_display = ["employee", "message", "created_at"]
    readonly_fields = ["created_at"]

admin.site.register(Task, TaskAdmin)
admin.site.register(Notification, NotificationAdmin)