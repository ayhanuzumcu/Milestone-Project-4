from django.test import TestCase
from .models import Product, Category


class TestProductsModels(TestCase):
    """
    Test the string methods return the correct model name fields
    """

    def test_products_string_method_returns_name(self):
        product = Product.objects.create(
            price=5.99,
            sku='abc123',
            name='Test Product',
            description='Test Product Description',
        )
        self.assertEqual(str(product), 'Test Product')

    def test_category_string_method_returns_display_name(self):
        category = Category.objects.create(
            name='Test Category',
            friendly_name='Test Friendly Name',
        )
        self.assertEqual(str(category), 'Test Category')
