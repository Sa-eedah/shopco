# from django.contrib.auth.models import User
# from django.db import models

# # Create your models here.
# class Category(models.Model):
#     # Category name
#     name = models.CharField(max_length=255)

#     class Meta:
#          # Sort categories alphabetically by name when queried
#         ordering = ('name',)
#         # Change plural display name in Django Admin from "Categorys" to "Categories"
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         # Display category name when the object is printed (e.g., in admin)
#         return self.name
# @property
# def items_count(self):
#     return self.items.count()

# # class Item(models.Model):
# #     # Each item belongs to a category
# #     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
# #     # Item's name
# #     name = models.CharField(max_length=255)
# #     # Description of item
# #     description = models.TextField(blank=True, null= True)
# #     # Price of Item
# #     price = models.FloatField()
# #     # Optional image upload (stored in 'media/item_images/')
# #     image = models.ImageField(upload_to='item_images', blank=True, null= True)
# #     # Boolean flag to mark if the item is already sold
# #     is_sold = models.BooleanField(default=False)
# #     # Link the item to the user who created it
# #     created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
# #     # Automatically store the date and time when the item was created
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         # Display the item name when the object is printed (e.g., in admin)
# #         return self.name

# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='items/')
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     description = models.TextField(blank=True, null=True)  # ✅ add this line
#     # is_sold = models.BooleanField(default=False)
#     # sold = models.IntegerField(default=0)  # For top selling

#     @property
#     def discount_price(self):
#         if self.original_price and self.price < self.original_price:
#             return self.price
#         return None

#     @property
#     def discount_percentage(self):
#         if self.discount_price:
#             return int(100 - (self.price / self.original_price * 100))
#         return 0

#     def __str__(self):
#         return self.name


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

