"""Serializer"""
from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    """Address serializer returns all data on Address from model"""
    class Meta:
        model = Address
        fields = ['id', 'zip', 'locality', 'streetAddress', 'extendedAddress']
