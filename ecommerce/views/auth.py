from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from ecommerce.models import User, Customer, Shop


def login_customer(request):
    return render(request, "login.html")


def login_customer_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('ecommerce:home')
    return render(request, "login.html", {"msg": "Invalid username/password"})


def logout_customer(request):
    logout(request)
    return redirect('ecommerce:home')


def register_custemer(request):
    return render(request, "register.html")


def register_customer_submit(request):
    # TODO: add register logic
    print('submit')
    return render(request, "login.html", {"msg": "Completed registration"})


def login_shop(request):
    return render(request, "login-shop.html")


def login_shop_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        shop = Shop.objects.get(owner=user)
        login(request, user)
        print(shop.owner_id)
        return redirect(reverse("ecommerce:shop-profile", kwargs={"shop_id": shop.owner_id}))
    return render(request, "login-shop.html", {"msg": "Shop does not exist"})
    