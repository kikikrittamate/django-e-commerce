from django.shortcuts import render


def products(request, category):
    # TODO: add query product with category
    return render(request, 'products.html')