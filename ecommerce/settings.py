import os
from pathlib import Path
import dj_database_url  # កុំភ្លេច install library នេះ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# ប្រើប្រាស់សញ្ញា || ដើម្បីកំណត់តម្លៃលំនាំដើមពេលអភិវឌ្ឍន៍លើកុំព្យូទ័រ
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-dev')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*'] # សម្រាប់ Railway គឺ * គឺងាយស្រួលបំផុត

# Database
# នេះគឺជាកន្លែងដែលយើងកែសម្រួលដើម្បីដោះស្រាយ Error របស់អ្នក
import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}
# សម្រាប់ Static files (សំខាន់សម្រាប់ Deployment)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# បញ្ជាក់៖ កុំភ្លេចបន្ថែម dj-database-url និង psycopg2-binary ក្នុង requirements.txt