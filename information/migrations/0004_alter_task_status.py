# Generated by Django 5.0.12 on 2025-03-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
