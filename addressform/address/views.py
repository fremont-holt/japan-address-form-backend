"""Address View"""
from django.shortcuts import render
from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer


class AddressView(viewsets.ModelViewSet):
    """Address model view set"""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
