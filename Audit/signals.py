from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now

from .models import AuditUserLogin


@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    """Logs user login time"""
    AuditUserLogin.objects.create(user=user, login_time=now())


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    """Updates logout time for the last recorded login"""
    last_login = AuditUserLogin.objects.filter(
        user=user, logout_time__isnull=True
    ).last()

    if last_login:
        last_login.logout_time = now()  # Update logout time
        last_login.save()
