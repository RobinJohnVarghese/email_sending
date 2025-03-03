
# path/to/your/proj/src/emailGeneration/celery.py
import os
from celery import Celery
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emailGeneration.settings')

app = Celery('emailGeneration')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

