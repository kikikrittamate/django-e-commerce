from django.shortcuts import render
from ..models import Item, Category


def products(request, category):
    category = Category.objects.get(name=category)
    items_list = Item.objects.filter(category=category, is_deleted=False)
    return render(request, 'products.html', { 'items_list': items_list, 'category': category })


def search_products(request):
    q = request.GET.get('products')
    items_list = Item.objects.filter(name__icontains=q, is_deleted=False)
    return render(request, 'products.html', { 'items_list': items_list, 'q': q })


def product_detail(request, product_id):
    try:
        product = Item.objects.get(id=product_id, is_deleted=False)
    except:
        return render(request, 'error/404.html')
    return render(request, 'product-detail.html', { 'item': product })