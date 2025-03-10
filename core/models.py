from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('role') != 'Admin':
            raise ValueError('Superuser must have role=Admin.')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("HOD", "HOD"),
        ("HR Manager", "HR Manager"),
        ("Employee", "Employee"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Employee")

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)

        # Ensure the user is added to the appropriate group based on their role
        group, created = Group.objects.get_or_create(name=self.role)
        self.groups.set([group])

        # Set superuser and staff status based on role
        if self.role == "Admin":
            self.is_superuser = True
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username