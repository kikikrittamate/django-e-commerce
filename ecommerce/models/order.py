from django.db import models
from django.contrib import admin
from .shop import Shop
from .item import Item
from .customer import Customer
import uuid


class Order(models.Model):
    ref = models.UUIDField(verbose_name="reference number", default=uuid.uuid4, editable=False, unique=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True)


    def get_shop(self):
        return self.item.shop


class OrderAdmin(admin.ModelAdmin):
    list_display = ('ref', 'customer', 'item', 'get_shop')