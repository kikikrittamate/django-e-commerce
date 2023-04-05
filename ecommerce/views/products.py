from django.shortcuts import render
from ..models import Item, Category


def products(request, category):
    # TODO: add query product with category
    category = Category.objects.get(name=category)
    items_list = Item.objects.filter(category=category)
    return render(request, 'products.html', { 'items_list': items_list })
