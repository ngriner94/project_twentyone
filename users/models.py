from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Hobby = models.CharField(max_length=255)



    