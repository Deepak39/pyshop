from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    Code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    discount = models.FloatField()