from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    password = models.CharField(max_length=100)

# Create your models here.
