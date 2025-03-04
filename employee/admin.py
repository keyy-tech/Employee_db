from django.contrib import admin
from .models import Employee, Department

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user','other_names', 'department', 'job_position', 'date_of_hire', 'employee_id', ]
    readonly_fields = ['employee_id']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'hod']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)