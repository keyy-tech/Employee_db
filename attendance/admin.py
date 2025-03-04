from django.contrib import admin
from .models import Attendance,Leave

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'check_in_time', 'check_out_time', 'total_working_hours']
    readonly_fields = ('total_working_hours',)
    

admin.site.register(Attendance, AttendanceAdmin)

class LeaveAdmin(admin.ModelAdmin):
    list_display = ['employee', 'leave_type', 'start_date', 'end_date', 'status']
    readonly_fields = ('status',)

admin.site.register(Leave, LeaveAdmin)