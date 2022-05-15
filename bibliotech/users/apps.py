"""
Users AppConfig module
See https://docs.djangoproject.com/en/4.0/ref/applications/#django.apps.AppConfig
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users AppConfig"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "bibliotech.users"
