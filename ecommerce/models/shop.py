from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Shop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, verbose_name="description")
    address = models.TextField()
    city = models.CharField(max_length=63)
    state = models.CharField(max_length=63)
    country = models.CharField(max_length=63)
    zipcode = models.CharField(max_length=63)
    phone = models.CharField(max_length=15)
    img = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name
    

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')