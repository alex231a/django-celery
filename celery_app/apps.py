"""Module apps"""

from django.apps import AppConfig


class CeleryAppConfig(AppConfig):
    """Class app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'celery_app'
