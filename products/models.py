from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    