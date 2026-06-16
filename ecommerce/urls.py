from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # រាល់ Request ដែលចាប់ផ្តើមដោយ 'products/' នឹងត្រូវបញ្ជូនទៅ products/urls.py
    path('products/', include('products.urls')), 
]