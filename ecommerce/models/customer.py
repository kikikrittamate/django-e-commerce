from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    city = models.CharField(max_length=63)
    state = models.CharField(max_length=63)
    country = models.CharField(max_length=63)
    zipcode = models.CharField(max_length=63)

    @property
    def customer_name(self):
        return self.user.first_name


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer_name')