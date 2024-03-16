from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            'date': '2024-03-15',
            'customer_name': 'Test Customer',
            'details': [
                {
                    'description': 'Test item 1',
                    'quantity': 1,
                    'unit_price': 10.00,
                    'price': 10.00
                }
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'Test Customer')

    # Add more test cases for other endpoints and scenarios
