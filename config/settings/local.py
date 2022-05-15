from .base import *
from .base import env

DEBUG = True


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
