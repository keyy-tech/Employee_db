from django.contrib import admin

from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("id", "table_name", "action_type", "action_time", "record_id")
    list_filter = ("table_name", "action_type")
    search_fields = ("table_name", "action_type", "record_id")

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def has_change_permission(self, request, obj=None):
        # Disable update
        return False

    def has_add_permission(self, request, obj=None):
        return False
