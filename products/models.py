from django.db import models
from django.contrib.auth.models import User

# ១. Model សម្រាប់ប្រភេទប្រភេទទំនិញ (ត្រូវនៅខាងលើគេ)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


# ២. Model សម្រាប់ទំនិញ (ត្រូវនៅពីលើ OrderItem ដើម្បីឱ្យគេអាចហៅទៅប្រើបាន)
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


# ៣. Model សម្រាប់រក្សាទុកព័ត៌មានអ្នកបញ្ជាទិញ
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name}"


# ៤. Model សម្រាប់រក្សាទុកមុខទំនិញលម្អិតដែលមាននៅក្នុងវិក្កយបត្រនីមួយៗ
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"