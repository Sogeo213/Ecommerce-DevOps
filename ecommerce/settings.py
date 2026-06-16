import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

# ត្រូវប្រាកដថាមាន admin ក្នុងនេះ
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orders',
    'products',
]

# កំណត់ Domain ដើម្បីដោះស្រាយ Error 403
CSRF_TRUSTED_ORIGINS = [
    'https://ecommerce-devops-production-62af.up.railway.app',
]

ROOT_URLCONF = 'ecommerce.urls'
WSGI_APPLICATION = 'ecommerce.wsgi.application'

# ការតភ្ជាប់ Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')