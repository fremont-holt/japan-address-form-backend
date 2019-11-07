"""Address Models"""
from django.db import models


class Address(models.Model):
    """
    Address has a zip, region, locality, streetAddress and an optional extendedAddress
    """
    zip = models.CharField(max_length=7)
    region = models.CharField(max_length=250)
    locality = models.CharField(max_length=250)
    streetAddress = models.CharField(max_length=250)
    extendedAddress = models.CharField(max_length=250, blank=True)
