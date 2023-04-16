from django.shortcuts import render
from ..models import Item, Category, Shop


def products(request, category):
    category = Category.objects.get(name=category)
    items_list = Item.objects.filter(category=category)
    return render(request, 'products.html', { 'items_list': items_list, 'category': category })


def search_products(request):
    q = request.GET.get('products')
    items_list = Item.objects.filter(name__icontains=q)
    return render(request, 'products.html', { 'items_list': items_list, 'q': q })


def product_detail(request, product_id):
    product = Item.objects.get(id=product_id)
    return render(request, 'product-detail.html', { 'item': product })

def add_item_shop_submit(request, shop_id):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    qty = request.POST.get('qty')
    price = request.POST.get('price')
    img = request.POST.get('img')
    category_id = request.POST.get('category')
    category = Category.objects.get(id=category_id)
    shop=Shop.objects.get(id=shop_id)
    
    # create item instance
    item = Item.objects.create(
        name = name,
        desc = desc,
        qty = qty,
        price = price,
        img = img,
        category = category,
        shop = shop,
    )
    return render(request, "shop-profile.html", {"msg": "เพิ่มสินค้าสำเร็จ"})