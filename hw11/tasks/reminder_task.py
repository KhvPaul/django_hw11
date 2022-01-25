from celery import Celery

from django.core.mail import send_mail

app = Celery('reminder_task', broker='pyamqp://guest@localhost//')


@app.task
def reminder(subject, datetime, text):
    send_mail(
        subject='Reminder',
        message=f'{datetime}: {text}',
        from_email="noreply@mysite.com",
        recipient_list=[subject],
    )
