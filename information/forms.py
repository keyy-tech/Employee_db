from django import forms

from employee.models import Employee
from .models import Task, Announcement


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["employee", "title", "description", "due_date"]
        labels = {
            "employee": "Employee",
            "title": "Title",
            "description": "Description",
            "due_date": "Due Date",
        }
        widgets = {
            "employee": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            if user.role == "HOD":
                self.fields["employee"].queryset = Employee.objects.filter(
                    department=user.employee.department
                ).exclude(user=user)
            elif user.role == "Admin":
                self.fields["employee"].queryset = Employee.objects.all()


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["title", "message"]
        labels = {
            "title": "Title",
            "message": "Message",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
