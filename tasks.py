import os

from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    # print('SUCCESS')
    os.system('python manage.py runserver')
    return x + y
