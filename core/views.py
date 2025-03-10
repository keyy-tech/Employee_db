from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, CustomPasswordChangeForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Redirect to a common dashboard
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid email or password")
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")


@login_required
def password_change_view(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect(
                "password_change"
            )  # Reload password change page after success
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, "core/password_change_form.html", {"form": form})


@login_required
def dashboard_view(request):
    # Get the user's role from their group
    user_role = None
    if request.user.is_superuser:
        user_role = "Admin"
    elif request.user.groups.filter(name="HOD").exists():
        user_role = "HOD"
    elif request.user.groups.filter(name="HR Manager").exists():
        user_role = "HR Manager"
    else:
        user_role = "Employee"

    return render(request, "core/dashboard.html", {"user_role": user_role})
