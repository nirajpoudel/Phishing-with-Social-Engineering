from django.db import models

# Create your models here.

class Details(models.Model):
    Username = models.CharField(max_length=100,null=True)
    Password = models.CharField(max_length=100, null=True)