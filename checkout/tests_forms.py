from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import OrderForm


class TestorderForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'county',
            'country'
        ))

    def test_firstname_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_telephone_is_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_addressline1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(
            form.errors['postcode'][0], 'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({'county': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('county', form.errors.keys())
        self.assertEqual(
            form.errors['county'][0], 'This field is required.')

    def test_country_is_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_remaining_fields_are_not_required(self):
        form = OrderForm({
            'full_name': 'Test',
            'email': 'test@email.com',
            'phone_number': '123456789',
            'street_address1': 'Test Address1',
            'town_or_city': 'Test Town',
            'postcode': 'test_code',
            'county': 'test',
            'country': 'GB'})
        self.assertTrue(form.is_valid())
