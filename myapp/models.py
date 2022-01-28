# Create your models here.
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()


class CustomerSettings(models.Model):
    preferred_color = models.CharField(max_length=24)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cus')
