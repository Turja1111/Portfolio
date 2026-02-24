"""
Development settings.
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email backend for dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
