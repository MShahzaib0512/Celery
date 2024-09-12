# celery.py
import os
from celery import Celery
from time import sleep
# from apk1.tasks import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

app = Celery('celeryapp')
app.conf.update(
    broker_url='redis://127.0.0.1:6379/0',
    result_backend='redis://127.0.0.1:6379/0',
    broker_transport_options={
        'visibility_timeout': 3600,  # Adjust as needed
    },
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def add(x,y):
 sleep(5)
 return x + y

@app.task
def ten(id):
    print('task runs')
    return id
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')