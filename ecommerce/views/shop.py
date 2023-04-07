from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import Shop, Item

def shop(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    print(shop.name)
    return render(request, 'shop.html', { 'shop': shop } )


@login_required(login_url="/shop/login")
def shop_profile(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    # deny access from everyone except for owner
    if shop.owner_id != request.user.id:
        return render(request, 'error/403.html', status=403)
    
    # TODO: add shop profile logic
    return render(request, 'shop-profile.html', { 'shop': shop } )