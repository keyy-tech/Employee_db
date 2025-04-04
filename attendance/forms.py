from django import forms

from .models import Leave


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
    employee_id = forms.CharField(
        label="Employee ID", widget=forms.TextInput(attrs={"class": "form-control"})
    )


class CheckOutForm(forms.Form):
    employee_id = forms.CharField(
        label="Employee ID", widget=forms.TextInput(attrs={"class": "form-control"})
    )
