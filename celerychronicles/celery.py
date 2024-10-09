import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerychronicles.settings")
app = Celery("celerychronicles")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.conf.task_routes = {
    'newapp.tasks.task1': 'queue1', 
    'newapp.tasks.task2': 'queue2'
}
app.autodiscover_tasks()


# @app.task
# def add():
#     return



