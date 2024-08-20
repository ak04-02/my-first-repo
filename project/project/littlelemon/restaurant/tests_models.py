
# Create your tests here.
# test_models.py
from django.test import TestCase
from .models import Menu, Booking
from django.utils import timezone

class MenuModelTests(TestCase):
    def test_string_representation(self):
        menu_item = Menu(name="Pasta", price=12,menu_item_description="something")
        self.assertEqual(str(menu_item), "Pasta")

    def test_price_format(self):
        menu_item = Menu(name="Pizza", price=15,menu_item_description="something")
        self.assertEqual(menu_item.price, 15)

class BookingModelTests(TestCase):
    def test_string_representation(self):
        booking = Booking(first_name="John",reservation_date="2015-02-02",reservation_slot="1")
        self.assertEqual(str(booking), "John")

    def test_booking_creation(self):
        booking = Booking.objects.create(first_name="Jane Doe", reservation_date="2015-02-02",reservation_slot="1")
        self.assertEqual(booking.first_name, "Jane Doe")
        