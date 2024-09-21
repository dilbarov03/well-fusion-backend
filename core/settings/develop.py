from .base import *  # noqa

DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True


CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "https://satyr-helped-intensely.ngrok-free.app/"
]