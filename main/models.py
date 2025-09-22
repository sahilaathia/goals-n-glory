from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('gloves', 'Gloves'),
        ('gear', 'Protective Gear'),
        ('training', 'Training Equipment'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=10, blank=True)
    color = models.CharField(max_length=50, blank=True)
    stock = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.brand} {self.name}"