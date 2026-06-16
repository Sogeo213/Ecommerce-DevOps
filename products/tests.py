from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product

class ProductSystemTest(TestCase):

    def setUp(self):
        # បង្កើតទិន្នន័យគំរូសម្រាប់ប្រើប្រាស់ក្នុងការតេស្ត
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Phone",
            description="A great phone",
            price=999.99,
            stock=10,
            category=self.category
        )

    # 🔄 Test 1: ពិនិត្យមើលការបង្កើត Category ក្នុង Database
    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")

    # 🔄 Test 2: ពិនិត្យមើលការបង្កើត Product ក្នុង Database
    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Phone")
        self.assertEqual(self.product.price, 999.99)

    # 🔄 Test 3: ពិនិត្យមើលការដំណើរការរបស់ទំព័រដើម (Homepage)
    def test_homepage_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Phone")

    # 🔄 Test 4: ពិនិត្យមើលការដំណើរការរបស់ទំព័រលម្អិតទំនិញ (Product Detail)
    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A great phone")

    # 🔄 Test 5: ពិនិត្យមើលដំណើរការ REST API (បោះទិន្នន័យជា JSON ត្រឹមត្រូវ)
    def test_api_product_list_view(self):
        response = self.client.get(reverse('api_product_list'))
        self.assertEqual(response.status_code, 200)
        # ពិនិត្យមើលថាទិន្នន័យដែលបោះមកជាទម្រង់ JSON
        self.assertEqual(response['content-type'], 'application/json')