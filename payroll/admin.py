from django.contrib import admin
from .models import Payroll

# Register your models here.
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['employee', 'basic_salary', 'bonuses', 'deductions', 'net_salary', 'payment_date']
    readonly_fields = ('net_salary', 'payment_date')

admin.site.register(Payroll, PayrollAdmin)