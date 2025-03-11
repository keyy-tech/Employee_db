from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Password reset paths
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="core/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="core/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="core/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="core/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # Password change paths
    path("password_change/", views.password_change_view, name="password_change"),
    path(
        "password_change_done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="core/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # Dashboard URL
    path("", views.dashboard_view, name="dashboard"),
]

# Custom error handlers
handler404 = views.custom_404_view
handler500 = views.custom_500_view
handler403 = views.custom_403_view
handler400 = views.custom_400_view
