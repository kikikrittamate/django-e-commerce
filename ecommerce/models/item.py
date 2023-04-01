from django.db import models
from django.contrib import admin
from .shop import Shop
from .category import Category


class Item(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, verbose_name="description")
    qty = models.IntegerField(default=0)
    price = models.FloatField()
    img = models.URLField(verbose_name="image url")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'shop', 'qty')