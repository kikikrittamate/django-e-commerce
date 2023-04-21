from django.db import models
from django.contrib import admin
from .shop import Shop
from .item import Item
from .customer import Customer
import uuid

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    is_ordered = models.BooleanField(default=False)

    def get_cart_total(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.item.price)
        return sum(price)




class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)

    def get_item_price(self):
        price = [self.item.price]
        return price