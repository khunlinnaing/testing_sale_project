from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    productimage = models.ImageField(upload_to='product_images/', blank=True, null=True)  # optional image
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    order_no = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_no
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.order_no:
            self.order_no = f"ORD-{self.id:05d}"
            super().save(update_fields=['order_no'])
