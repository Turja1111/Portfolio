import os
from .base import *  # noqa: F401, F403

DEBUG = os.environ.get('DEBUG', 'False') != 'False'

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-prod-pa-Turja221b-8fKp2qX9mV7zR4sL1nB6cD3hY0aW5eU',
)

ALLOWED_HOSTS = [
    'Turja221b.pythonanywhere.com',
    'localhost',
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CHATBOT_USE_DEEPSEEK = os.environ.get('CHATBOT_USE_DEEPSEEK', 'False').lower() == 'true'
CHATBOT_USE_OPENROUTER = os.environ.get('CHATBOT_USE_OPENROUTER', 'False').lower() == 'true'
