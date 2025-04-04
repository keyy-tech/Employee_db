# Generated by Django 5.0.12 on 2025-03-04 01:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0003_employee_other_names"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("check_in_time", models.TimeField(blank=True, null=True)),
                ("check_out_time", models.TimeField(blank=True, null=True)),
                (
                    "total_working_hours",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employee.employee",
                    ),
                ),
            ],
        ),
    ]
