from django.shortcuts import render, redirect
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
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    shop = Shop.objects.get(owner_id=shop_id)
    items = Item.objects.filter(shop=shop)

    # TODO: add shop profile logic
    
    return render(request, 'shop-profile.html', { 'shop': shop, 'items': items } )


@login_required(login_url="/shop/login")
def shop_add(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    shop=Shop.objects.get(owner_id=shop_id)
    categories = Category.objects.all()
    return render(request, 'shop-add.html', { 'shop': shop, 'categories': categories })


@login_required(login_url="/shop/login")
def add_item_shop_submit(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
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
    return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}))

@login_required(login_url="/shop/login")
def delete_item(request, shop_id, item_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    item = Item.objects.get(id=item_id)
    item.delete()
    shop=Shop.objects.get(owner_id=shop_id)
    return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}))
