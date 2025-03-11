from django.db.models.signals import post_save
from django.dispatch import receiver

from attendance.models import Attendance, Leave
from employee.models import Employee
from information.models import Task, Announcement, Notification
from payroll.models import Payroll


# 1️⃣ Employee Creation & Update
@receiver(post_save, sender=Employee)
def notify_employee_created_or_updated(sender, instance, created, **kwargs):
    if created:
        message = f"🎉 Welcome {instance.user.first_name}, your employee profile has been created successfully!"
    else:
        message = f"🔄 Your employee profile has been updated."

    Notification.objects.create(employee=instance, message=message)


# 2️⃣ Payroll Processed & Updated
@receiver(post_save, sender=Payroll)
def notify_payroll_processed_or_updated(sender, instance, created, **kwargs):
    if created:
        message = f"💰 Payroll processed! Your salary for {instance.payment_date.strftime('%B %Y')} is ready."
    else:
        message = f"🔄 Payroll updated! Your salary details for {instance.payment_date.strftime('%B %Y')} have been modified."

    Notification.objects.create(employee=instance.employee, message=message)


# 3️⃣ Task Assigned & Completed
@receiver(post_save, sender=Task)
def notify_task_updates(sender, instance, created, **kwargs):
    if created:
        message = f"📌 New Task Assigned: {instance.title}. Due by {instance.due_date}."
    elif instance.status.lower() == "completed":
        message = f"✅ Task Completed: {instance.title}. Well done!"
    elif instance.status.lower() == "important":
        message = f"⚠️ Important Task: {instance.title}. Please prioritize!"

    Notification.objects.create(employee=instance.employee, message=message)


# 4️⃣ Leave Approval & Rejection
@receiver(post_save, sender=Leave)
def notify_leave_status(sender, instance, **kwargs):
    if instance.status.lower() == "approved":
        message = f"✅ Your leave from {instance.start_date} to {instance.end_date} has been approved. Enjoy your time off!"
    elif instance.status.lower() == "rejected":
        message = f"❌ Your leave request from {instance.start_date} to {instance.end_date} was rejected. Contact HR for details."

    Notification.objects.create(employee=instance.employee, message=message)


# 5️⃣ Check-In & Check-Out
@receiver(post_save, sender=Attendance)
def notify_attendance(sender, instance, created, **kwargs):
    if instance.check_in_time and not instance.check_out_time:
        message = f"🕒 You checked in at {instance.check_in_time.strftime('%H:%M')}. Have a productive day!"
    elif instance.check_out_time:
        message = f"🏁 You checked out at {instance.check_out_time.strftime('%H:%M')}. See you tomorrow!"

    Notification.objects.create(employee=instance.employee, message=message)


# 6️⃣ Announcements
@receiver(post_save, sender=Announcement)
def notify_announcement(sender, instance, created, **kwargs):
    if created:
        message = f"📢 New Announcement: {instance.title} - {instance.content[:50]}..."
        Notification.objects.create(employee=instance.employee, message=message)
