from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)