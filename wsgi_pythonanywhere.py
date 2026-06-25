import os
import sys

PROJECT_DIR = '/home/Turja221b/Portfolio'
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings.pythonanywhere'
os.environ['PYTHONANYWHERE_USERNAME'] = 'Turja221b'
os.environ['PYTHONANYWHERE_DOMAIN'] = 'Turja221b.pythonanywhere.com'
os.environ['SECRET_KEY'] = 'django-prod-pa-Turja221b-8fKp2qX9mV7zR4sL1nB6cD3hY0aW5eU'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
