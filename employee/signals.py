from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def assign_role_to_group(sender, instance, created, **kwargs):
    if created or instance.role:  # If new user or role changed
        # Get or create the group based on the user's role
        group, _ = Group.objects.get_or_create(name=instance.role)

        # Remove user from all other groups and assign the new group
        instance.groups.clear()
        instance.groups.add(group)
