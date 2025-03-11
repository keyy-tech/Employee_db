from django import forms

from employee.models import Employee
from .models import Leave, Attendance


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = [
            "leave_type",
            "start_date",
            "end_date",
        ]
        labels = {
            "employee": "Employee",
            "leave_type": "Leave Type",
            "start_date": "Start Date",
            "end_date": "End Date",
        }
        widgets = {
            "leave_type": forms.Select(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class CheckInForm(forms.Form):
    employee_id = forms.IntegerField(label="Employee ID", widget=forms.NumberInput(attrs={"class": "form-control"}))

class CheckOutForm(forms.Form):
    employee_id = forms.IntegerField(label="Employee ID", widget=forms.NumberInput(attrs={"class": "form-control"}))