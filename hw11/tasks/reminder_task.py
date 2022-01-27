from celery import shared_task

from django.core.mail import send_mail


@shared_task
def reminder(subject, datetime, text):
    send_mail(
        subject='Reminder',
        message=f'{datetime}: {text}',
        from_email="noreply@mysite.com",
        recipient_list=[subject],
    )
