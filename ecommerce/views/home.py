from django.shortcuts import render
from ecommerce.models import Category


def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})