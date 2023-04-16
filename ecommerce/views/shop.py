from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import Shop, Item, Category
from django.contrib.auth.models import User

def shop(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    items = Item.objects.filter(shop=shop)
    print(shop.name)
    return render(request, 'shop.html', { 'shop': shop, 'items': items} )


@login_required(login_url="/shop/login")
def shop_profile(request, shop_id):
    shop = Shop.objects.get(owner_id=shop_id)
    items = Item.objects.filter(shop=shop)
    # deny access from everyone except for owner
    if shop.owner_id != request.user.id:
        return render(request, 'error/403.html', status=403)
    
    # TODO: add shop profile logic
    
    return render(request, 'shop-profile.html', { 'shop': shop, 'items': items } )

def shop_add(request, shop_id):
    shop=Shop.objects.get(owner_id=shop_id)
    return render(request, 'shop-add.html', { 'shop': shop})

def add_item_shop_submit(request, shop_id):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    qty = request.POST.get('qty')
    price = request.POST.get('price')
    img = request.POST.get('img')
    category_id = request.POST.get('category')
    category = Category.objects.get(id=category_id)
    shop=Shop.objects.get(owner_id=shop_id)
    
    # create item instance
    item = Item.objects.create(
        name = name,
        desc = desc,
        qty = qty,
        price = price,
        img = img or "",
        category = category,
        shop = shop,
    )
    return render(request, 'shop-profile.html', {"msg": "เพิ่มสินค้าสำเร็จ"})