from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import Shop, Item, Category, Order
import requests
import os
from webapp.settings import IMAGE_API_ROOT, IMAGE_API_TOKEN, S3_URL

def shop(request, shop_id):
    try:
        shop = Shop.objects.get(owner_id=shop_id)
    except Shop.DoesNotExist:
        return render(request, 'error/404.html')
    items = Item.objects.filter(shop=shop, is_deleted=False)
    return render(request, 'shop.html', { 'shop': shop, 'items': items} )


@login_required(login_url="/shop/login")
def shop_profile(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    try:
        shop = Shop.objects.get(owner_id=shop_id)
    except Shop.DoesNotExist:
        return render(request, 'error/404.html')
    items = Item.objects.filter(shop=shop)    
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

    category_id = request.POST.get('category')
    category = Category.objects.get(id=category_id)
    shop=Shop.objects.get(owner_id=shop_id)
    
    # create item instance
    item = Item.objects.create(
        name = name,
        desc = desc,
        qty = qty,
        price = price,
        category = category,
        shop = shop,
    )

    # upload image
    img = request.FILES['img']
    upload_image(img.file, f"item-{item.id}.jpg")
    item.img = os.path.join(S3_URL, f"item-{item.id}.jpg")
    item.save()

    return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}))

@login_required(login_url="/shop/login")
def delete_item(request, shop_id, item_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    item = Item.objects.get(id=item_id)
    item.is_deleted = True
    item.save()
    shop=Shop.objects.get(owner_id=shop_id)
    return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}))


@login_required(login_url="/shop/login")
def shop_edit(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    shop=Shop.objects.get(owner_id=shop_id)
    return render(request, 'edit-shop-profile.html', { 'shop': shop })


@login_required(login_url="/shop/login")
def edit_shop_profile_submit(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    shop = Shop.objects.get(owner_id=shop_id)
    if request.method == "POST":
        shop.desc = request.POST.get('desc')
        shop.address = request.POST.get('address')
        shop.city = request.POST.get('city')
        shop.state = request.POST.get('state')
        shop.country = request.POST.get('country')
        shop.zipcode = request.POST.get('zipcode')
        shop.phone = request.POST.get('phone')
        shop.img = request.POST.get('img')
        shop.owner.email = request.POST.get('email')
        shop.save()
        shop.owner.save()
    context={ 'shop': shop }
    return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}), context)


def upload_image(content, fname):
    url = os.path.join(IMAGE_API_ROOT, fname)
    payload = content
    headers = {
    'x-api-key': IMAGE_API_TOKEN,
    'Content-Type': 'image/jpeg'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.status_code)

@login_required(login_url="/shop/login")
def shop_order(request, shop_id):
    if request.user.id != shop_id:
        # msg: You are not shop owner
        return render(request, 'error/403.html', status=403)
    shop=Shop.objects.get(owner_id=shop_id)
    return render(request, 'order.html', { 'shop': shop })
