import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies_project.settings")

app = Celery("movies_project")
app.config_from_object("django.conf:settings", namespace="CELERY")


# import os
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_project.settings')
#
# app = Celery('movies_project')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
# # celery brat tasks
#
# app.conf.beat_schedule = {
#     'send-spam-every-10-minute': {
#         'task': 'email.tasks.send_beat_email',
#         'schedule': crontab(minute='*/10'),
#     },
# }
