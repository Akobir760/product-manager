from django.db import models

# Create your models here.

class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"ID {self.id}) {self.name}  |  {self.quantity}"
    

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'