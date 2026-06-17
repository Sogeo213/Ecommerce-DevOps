from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # ១. បន្ថែមការ Import នេះ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    
    # ២. បន្ថែមបន្ទាត់នេះ ដើម្បីបង្វែរទំព័រដើមទៅកាន់បញ្ជីផលិតផល
    path('', RedirectView.as_view(url='/products/list/', permanent=True)), 
]