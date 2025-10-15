from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rating = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)  # ✅ added safely
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # ✅ safe optional image
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

