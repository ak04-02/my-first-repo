from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Menu,Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Menu
        fields='__all__'
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'