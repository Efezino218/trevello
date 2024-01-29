from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100000)
    price = models.CharField(max_length=50)
