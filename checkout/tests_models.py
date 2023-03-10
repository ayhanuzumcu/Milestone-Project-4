from django.test import TestCase
from .models import (
    Order, OrderLineItem)
from products.models import Product


class TestCheckoutModels(TestCase):
    """
    Test the string methods return the correct model name fields
    """

    def setUp(self):
        self.product = Product.objects.create(
            price=5.99,
            sku='abc123',
            name='Test Product',
            description='Test Product Description',
        )
        self.order = Order.objects.create(
            order_number='Test Order',
            date='2021-05-09 14:30:59',
            full_name='John',
            email='test@email.com',
            phone_number='123456789',
            street_address1='Address Line 1',
            street_address2='Address Line 2',
            town_or_city='City',
            postcode='AB99-XYZ',
            county='County',
            country='GB',
            delivery_cost=2.50,
            order_total=10.99,
            grand_total=13.49,
        )

    def test_order_string_method_returns_order_number(self):
        order = Order.objects.get(
            order_number='Test Order'
        )
        self.assertEqual(str(order), 'Test Order')
