from django.shortcuts import render
from ..models import Shop, Item


def shop(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    print(shop.name)
    return render(request, 'shop.html', { 'shop': shop } )


def shop_profile(request, shop_id):
    # TODO: replace this with shop profile page logics
    shop = Shop.objects.get(owner_id=shop_id)
    # TODO: deny access from everyone except for owner
    print(shop.name)
    return render(request, 'shop-profile.html', { 'shop': shop } )