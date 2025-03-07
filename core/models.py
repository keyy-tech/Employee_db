from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("HR", "HR"),
        ("Manager", "Manager"),
        ("Employee", "Employee"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="employee")

    def save(self, *args, **kwargs):
        if self.role == "admin":
            self.is_superuser = True
            self.is_staff = True
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
