from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import OrderCreateForm
from django.http import JsonResponse
from .models import Product
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name='product-list'),
    path('detail/<int:product_id>/', views.product_detail, name='product-detail'),
]

# ១. ទំព័របង្ហាញបញ្ជីទំនិញទាំងអស់
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# កែប្រែត្រង់នេះនៅក្នុង products/views.py 
def product_detail(request, product_id): # <--- ប្រើ product_id ឱ្យត្រូវនឹង urls.py
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

# ៣. មុខងារបន្ថែមទំនិញចូលទៅក្នុងកន្ត្រក (Cart)
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        }
        
    request.session['cart'] = cart
    return redirect('cart_detail')

# ៤. ទំព័របង្ហាញមុខទំនិញនៅក្នុងកន្ត្រក
def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0.0
    
    for item_id, item_data in cart.items():
        subtotal = item_data['price'] * item_data['quantity']
        total_price += subtotal
        cart_items.append({
            'id': item_id,
            'name': item_data['name'],
            'price': item_data['price'],
            'quantity': item_data['quantity'],
            'subtotal': subtotal
        })
        
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'products/cart_detail.html', context)

# ៥. មុខងារសម្អាតទំនិញចេញពីកន្ត្រក
def cart_clear(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('product_list')

# ៦. ទំព័រទូទាត់ប្រាក់ (Checkout) - តម្រូវឱ្យ Login ជាមុនសិន
@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('product_list')
        
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # ភ្ជាប់ការទិញទៅកាន់គណនីដែលកំពុងប្រើ
            order.total_price = total_price
            order.ordered = True
            order.save()
            
            for item_id, item_data in cart.items():
                product = get_object_or_404(Product, id=int(item_id))
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=item_data['price'],
                    quantity=item_data['quantity']
                )
                
            request.session['cart'] = {}
            return redirect('order_success', order_id=order.id)
    else:
        form = OrderCreateForm()
        
    return render(request, 'products/checkout.html', {'form': form, 'cart': cart, 'total_price': total_price})

# ៧. ទំព័រជោគជ័យក្រោយពេលទិញរួច
def order_success(request, order_id):
    return render(request, 'products/order_success.html', {'order_id': order_id})


# ==================== ប្រព័ន្ធគ្រប់គ្រងគណនីសមាជិក (Authentication) ====================

# ៨. មុខងារចុះឈ្មោះសមាជិកថ្មី (Register)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})

# ៩. មុខងារចូលប្រើប្រាស់ប្រព័ន្ធ (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'products/login.html', {'form': form})

# ១០. មុខងារចាកចេញពីប្រព័ន្ធ (Logout)
def logout_view(request):
    logout(request)
    return redirect('product_list')

# ១១. ទំព័រមើលប្រវត្តិនៃការបញ្ជាទិញ (Order History)
@login_required(login_url='login')
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'products/order_history.html', {'orders': orders})

def api_product_list(request):
    # ទាញយកទំនិញទាំងអស់ជាទម្រង់ Dictionary (id, name, price, stock)
    products = Product.objects.all().values('id', 'name', 'price', 'stock')
    
    # បោះទិន្នន័យត្រឡប់ទៅវិញជាទម្រង់ JSON
    return JsonResponse(list(products), safe=False, json_dumps_params={'ensure_ascii': False})