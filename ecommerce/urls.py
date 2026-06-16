from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # 🎯 ផ្លូវ Admin ពិតប្រាកដគឺនៅទីនេះតែមួយគត់!
    path('', include('products.urls')), # <--- ទាញយកផ្លូវទាំងអស់ពី products/urls.py មកប្រើ
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)