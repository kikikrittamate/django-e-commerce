from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Order, OrderAdmin)