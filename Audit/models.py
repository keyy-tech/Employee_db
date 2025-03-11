from django.db import models


class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    action_type = models.CharField(max_length=10)  # INSERT, UPDATE, DELETE
    action_time = models.DateTimeField(auto_now_add=True)
    record_id = models.BigIntegerField()

    class Meta:
        db_table = "audit_log_154"
        managed = False
