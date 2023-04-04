from django.shortcuts import render
from ..models import Item

def products(request, category):
    context = {'items_list':Item.objects.all()}
    return render(request, 'products.html', context)