from django import forms

from .models import Task


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
