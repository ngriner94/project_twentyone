from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    hobby = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)




    