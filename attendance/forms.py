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


class AttendanceForm(forms.ModelForm):
    employee_id = forms.CharField(
        max_length=100,
        label="Employee ID",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Attendance
        fields = ["employee_id"]
        labels = {
            "employee_id": "Employee ID",
        }
        widgets = {
            "employee_id": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_employee_id(self):
        employee_id = self.cleaned_data.get("employee_id")
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise forms.ValidationError("Employee with this ID does not exist.")
        return employee_id

    def save(self, commit=True):
        attendance = super().save(commit=False)
        employee_id = self.cleaned_data.get("employee_id")
        attendance.employee = Employee.objects.get(employee_id=employee_id)
        if commit:
            attendance.save()
        return attendance
