"""
Development settings.
"""
from .base import *  # noqa: F401, F403
from .base import postgres_database_config

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': postgres_database_config()
}

# Email backend for dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
