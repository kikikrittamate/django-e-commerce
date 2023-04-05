from django.shortcuts import render
from ..models import Item, Category


def products(request, category):
    category = Category.objects.get(name=category)
    items_list = Item.objects.filter(category=category)
    return render(request, 'products.html', { 'items_list': items_list })


def search_products(request):
    q = request.GET.get('products')
    print("this is request", q)
    items_list = []
    return render(request, 'products.html', { 'items_list': items_list })
