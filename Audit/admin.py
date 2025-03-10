from django.contrib import admin

from .models import AuditUserLogin


@admin.register(AuditUserLogin)
class AuditUserLoginAdmin(admin.ModelAdmin):
    list_display = ("user", "login_time", "logout_time")  # Show fields
    readonly_fields = (
        "user",
        "login_time",
        "logout_time",
    )  # Make all fields read-only

    def has_add_permission(self, request):
        return False  # Prevent adding records manually

    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing records

    def has_delete_permission(self, request, obj=None):
        return False  # Prevent deleting records
