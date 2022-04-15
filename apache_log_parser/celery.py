import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apache_log_parser.settings")
app = Celery("apache_log_parser")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
