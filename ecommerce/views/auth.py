from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ecommerce.models import User, Customer, Shop


def login_customer(request):
    return render(request, "login.html")


def login_customer_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(request.POST.get('username'))
    if user is not None:
        login(request, user)
        return redirect('ecommerce:home')
    return render(request, "login.html", {"msg": "Invalid username/password"})


def logout_customer(request):
    logout(request)
    return redirect('ecommerce:home')


def register_custemer(request):
    return render(request, "register.html") 