from django.test import TestCase, Client
from django.urls import reverse
from .views import menu,bookings
class MyViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request_menu(self):
        response = self.client.get(reverse(menu))
        self.assertEqual(response.status_code, 200)

    def test_get_request_booking(self):
        response = self.client.get(reverse(bookings))
        self.assertEqual(response.status_code, 200)