import os
from django.core.wsgi import get_wsgi_application

# ត្រូវប្រាកដថាវាចង្អុលទៅ settings ត្រឹមត្រូវ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()