# Create your models here.
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.age} years old'


class CustomerSettings(models.Model):
    preferred_color = models.CharField(max_length=24)
    customer = models.OneToOneField('myapp.Customer', on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f'{self.customer} like {self.preferred_color}.'
