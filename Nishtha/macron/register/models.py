from __future__ import unicode_literals

from django.db import models

# Create your models here.
LANGUAGES = (
              (0, "English"),
              (1, "Hindi"),
              (2, "Punjabi"),
              (3, "Gujarati"),
              (4, "Tamil"),
              (5, "Telugu"),
              (6, "Bengali")
            )


class Customer(models.Model):
    phone = models.IntegerField(primary_key=True)
    aadhar = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    balance = models.IntegerField()
    address = models.CharField(max_length=500)
    bank = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    geo_location = models.CharField(max_length=100)
    language = models.IntegerField(choices=LANGUAGES)
