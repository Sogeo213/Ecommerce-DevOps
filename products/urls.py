from django.urls import path
from . import views

urlpatterns = [
    # ទំព័រដើម Catalog
    path('', views.product_list, name='product_list'),
    
    # ទំព័រលម្អិតទំនិញ (បានកែសម្រួលប្រើ product_id និងលុបខ្សែដែលប្រើ pk ចោលដើម្បីកុំឱ្យជាន់គ្នា)
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # ប្រព័ន្ធកន្ត្រកទំនិញ (Shopping Cart)
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    
    # ប្រព័ន្ធឆែកឡៅត៍ (Checkout)
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<int:order_id>/', views.order_success, name='order_success'),
    
    # ប្រព័ន្ធគណនីសមាជិក (Authentication)
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', views.order_history, name='order_history'),
    
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('api/products/', views.api_product_list, name='api_product_list'),
    
    # 🎯 ថែមបន្ទាត់នេះចូល ដើម្បីបង្កើតផ្លូវ REST API របស់លោកអ្នក
    path('api/products/', views.api_product_list, name='api_product_list'),
]