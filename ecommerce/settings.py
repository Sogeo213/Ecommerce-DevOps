import os
from pathlib import Path

# 1. ផ្លូវដើមនៃ Project (Base Directory)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. ការកំណត់ប្រព័ន្ធសុវត្ថិភាព (Security Settings)
# នៅលើ Production (Railway) វាទាញយក Key ពី Environment Variables បើគ្មានវាប្រើ Key Fallback
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-y3^=^@)90s-&1892h_#=)028=3_@')

# បើក DEBUG = True ដើម្បីមើល Error ចំៗពេលកំពុងដោះស្រាយ ប្តូរទៅ False ពេលហ្គេមហ្ស៊ីន
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# អនុញ្ញាតឱ្យរត់លើរាល់ Domain ទាំងអស់របស់ Railway
ALLOWED_HOSTS = ['*']


# 3. ការប្រកាស App ទាំងអស់ (ចំណុចសំខាន់ដែលធ្វើឱ្យបាត់ Error Template)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # ត្រូវប្រាកដថាមានឈ្មោះ App របស់អ្នកនៅទីនេះ (មានអក្សរ s ខាងចុង)
    'products', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # សម្រាប់គ្រប់គ្រង Static Files លើ Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

# 4. ការកំណត់រចនាសម្ព័ន្ធ Templates (ចំណុចសំខាន់ទី២ សម្រាប់ស្វែងរកឯកសារ HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # ស្វែងរកក្នុង Folder templates រួម (បើមាន)
        'APP_DIRS': True,                  # ត្រូវតែ True ដើម្បីឱ្យវាចូលទៅកកាយក្នុង products/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# 5. ការកំណត់ប្រព័ន្ធទិន្នន័យ (Database)
# ប្រើប្រាស់ SQLite ជាបណ្តោះអាសន្ន (ឬផ្លាស់ប្តូរតាម PostgreSQL បើអ្នកបានភ្ជាប់វាលើ Railway)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 6. ការផ្ទៀងផ្ទាត់លេខកូដសម្ងាត់ (Password Validation)
AUTH_PASSWORD_VALIDATORS =