from django.shortcuts import render
from ..models import Shop, Item


def shop(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    items = Item.objects.filter(shop=shop)
    print(shop.name)
    return render(request, 'shop.html', { 'shop': shop, 'items': items} )