from django.shortcuts import render
from django.views import generic
from ..models import Item


class ProductsView(generic.ListView):
    template_name = 'ecommerce/products.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        return Item.objects.filter().order_by(__name__)
    
def products(request):
    return render(request, 'products.html')