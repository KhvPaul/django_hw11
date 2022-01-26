import os

from celery import Celery, shared_task

from django.core.mail import send_mail

app = Celery('reminder_task', broker='pyamqp://guest@localhost//')


@app.task
# @shared_task  ?
def reminder(subject, datetime, text):
    # os.system('export DJANGO_SETTINGS_MODULE=hw11_core.settings')
    # os.system('python manage.py runserver')
    send_mail(
        subject='Reminder',
        message=f'{datetime}: {text}',
        from_email="noreply@mysite.com",
        recipient_list=[subject],
    )
