from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm,AnnouncementForm
from .models import Task,Announcement


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = "Pending"
            task.save()
            messages.success(request, "Task created successfully")
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/create.html", {"form": form})


@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if task.status in ["Complete", "Not Complete"]:
        messages.error(request, "Task cannot be updated because it is marked as complete or not complete")
        return redirect("task_list")
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update.html", {"form": form, "task": task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status in ["Complete", "Not Complete"]:
        messages.error(request, "Task cannot be deleted because it is marked as complete or not complete")
        return redirect("task_list")
    
    task.delete()
    messages.success(request, "Task deleted successfully")
    return redirect("task_list")


@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/list.html", {"tasks": tasks})


@login_required
def user_tasks(request):
    tasks = Task.objects.filter(employee=request.user.employee)
    return render(request, "tasks/user_tasks.html", {"tasks": tasks})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status == "Complete":
        messages.error(request, "Task is already marked as complete")
    elif task.status == "Not Complete":
        messages.error(request, "Task cannot be marked as complete because it is marked as not complete")
    else:
        task.status = "Complete"
        task.save()
        messages.success(request, "Task marked as complete")
    return redirect('task_list')


@login_required
def incomplete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.status == "Not Complete":
        messages.error(request, "Task is already marked as not complete")
    elif task.status == "Complete":
        messages.error(request, "Task cannot be marked as not complete because it is marked as complete")
    else:
        task.status = "Not Complete"
        task.save()
        messages.success(request, "Task marked as not complete")
    return redirect('task_list')


@login_required
def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, "announcements/list.html", {"announcements": announcements})

@login_required
def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, "announcements/detail.html", {"announcement": announcement})

@login_required
def create_announcement(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Announcement created successfully")
            return redirect("announcement_list")
    else:
        form = AnnouncementForm()
    return render(request, "announcements/create.html", {"form": form})

@login_required
def update_announcement(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, "Announcement updated successfully")
            return redirect("announcement_list")
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, "announcements/update.html", {"form": form})

@login_required
def delete_announcement(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    if request.method == "POST":
        announcement.delete()
        messages.success(request, "Announcement deleted successfully")
        return redirect("announcement_list")
    return render(request, "announcements/delete.html", {"announcement": announcement})