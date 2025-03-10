from django import forms
from .models import Employee, Department
from core.models import CustomUser


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "hod"]
        labels = {
            "name": "Department Name",
            "hod": "Head of Department",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "hod": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correct indentation here
        if "hod" in self.fields:  # Ensure 'hod' exists in form fields
            self.fields["hod"].queryset = Employee.objects.filter(user__role="HOD")


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user', 'employee_id']
        labels = {
            'other_names': 'Other Names',
            'phone': 'Phone Number',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'department': 'Department',
            'job_position': 'Job Position',
            'date_of_hire': 'Date of Hire',
            'address': 'Address',
            'emergency_contact_name': 'Emergency Contact Name',
            'emergency_contact_phone': 'Emergency Contact Phone',
        }
        widgets = {
            'other_names': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'job_position': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_hire': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
