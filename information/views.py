from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC CreateTask @employee_id=%s, @title=%s, @description=%s, @due_date=%s, @status=%s",
                    [
                        data["employee"].id,
                        data["title"],
                        data["description"],
                        data["due_date"],
                        "Pending",
                    ],
                )
            messages.success(request, "Task created successfully")
            return redirect("task_list")

    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_update.html", {"form": form, "task": task})


@login_required
def delete_task(request, task_id):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("EXEC DeleteTask @task_id=%s", [task_id])
        messages.success(request, "Task Deleted Successfully")
        return redirect("task_list")


@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})
