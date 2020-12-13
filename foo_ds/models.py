from django.db import models


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=1000, default="")
    sid = models.CharField(max_length=1000, default="")
    price = models.CharField(max_length=1000, default="")
    desc = models.CharField(max_length=10000, default="")
    catname = models.CharField(max_length=10000, default="")
    image = models.ImageField(upload_to='')