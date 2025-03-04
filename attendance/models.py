from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from employee.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    total_working_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"

    def calculate_working_hours(self):
        if self.check_in_time and self.check_out_time:
            check_in = datetime.combine(self.date, self.check_in_time)
            check_out = datetime.combine(self.date, self.check_out_time)

            if check_out <= check_in:
                return 0

            total_duration = check_out - check_in

            if total_duration.total_seconds() < 0:
                return 0

            return round(total_duration.total_seconds() / 3600, 2)  # Return hours as decimal
        return None

    def save(self, *args, **kwargs):
        self.total_working_hours = self.calculate_working_hours()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "attendance_154"
        managed = True


class Leave(models.Model):
    LEAVE_TYPES = [
        ("Sick", "Sick Leave"),
        ("Vacation", "Vacation"),
        ("Unpaid", "Unpaid Leave"),
        ("Maternity", "Maternity Leave"),
        ("Paternity", "Paternity Leave"),
        ("Bereavement", "Bereavement Leave"),
        ("Study", "Study Leave"),
        ("Compassionate", "Compassionate Leave"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type} ({self.status})"
    class Meta:
        db_table = "leave_154"
        managed = True