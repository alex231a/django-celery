"""Module with celery config"""

from __future__ import absolute_import

import os

from celery import Celery  # pylint: disable=E0401

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson_forms.settings')

app = Celery("cworker")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
