from django.db import models
from django.contrib import admin
from .shop import Shop
from .item import Item
from .customer import Customer
import uuid

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    is_ordered = models.BooleanField(default=False)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)