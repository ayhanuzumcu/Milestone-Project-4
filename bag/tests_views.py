from django.test import TestCase


class TestBagViews(TestCase):
    """
    Tests the home page renders the correct page
    """
    def test_shopping_cart_page(self):
        response = self.client.get('/bag', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'bag/bag.html')
