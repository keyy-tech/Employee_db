from django.db import models
from django.utils.timezone import now

from core.models import CustomUser


class AuditUserLogin(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=now)
    logout_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "audit_user_login_154"
        managed = False  # Assuming this table is managed externally

    def __str__(self):
        return f"{self.user.employee.employee_id} - {self.login_time}"
