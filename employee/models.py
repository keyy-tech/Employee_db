import uuid

from django.db import models

from core.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="headed_departments",
    )

    class Meta:
        db_table = "department_154"
        managed = True

    def __str__(self):
        return self.name


class Employee(models.Model):
    # Personal Information
    other_names = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender_choices = [("Male", "Male"), ("Female", "Female")]
    gender = models.CharField(max_length=100, choices=gender_choices)

    # Employment Information
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE, blank=True, null=True
    )
    job_position = models.CharField(max_length=100)
    date_of_hire = models.DateField()
    employee_id = models.CharField(max_length=100, editable=False)

    # Address & Emergency Contact
    address = models.CharField(max_length=100)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=10)

    class Meta:
        db_table = "employee_154"
        managed = True

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        if not self.employee_id and self.user.first_name and self.user.last_name:
            unique_id = uuid.uuid4().hex[:10].upper()
            self.employee_id = f"{self.user.first_name[0].upper()}{self.user.last_name[0].upper()}-{unique_id}"
        super().save(*args, **kwargs)
