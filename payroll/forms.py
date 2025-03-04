from django import forms
from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        exclude = ['net_salary', 'payment_date', 'employee']
        labels = {
            'basic_salary': 'Basic Salary',
            'bonuses': 'Bonuses',
            'deductions': 'Deductions',
            'bank_name': 'Bank Name',
            'account_name': 'Account Name',
            'account_number': 'Account Number',
        }
        widgets = {
            'basic_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'bonuses': forms.NumberInput(attrs={'class': 'form-control'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
        }