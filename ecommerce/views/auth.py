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
    username = request.POST.get('username')
    password = request.POST.get('password')
    cf_password = request.POST.get('cf-password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('lastname')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    zipcode = request.POST.get('zipcode')
    # validate
    if not validate_username(username):
        return render(request, "register.html", {"msg": "Username already exist"})
    if not validate_password(password, cf_password):
        return render(request, "register.html", {"msg": "Invalid password or confirm password"})
    # create base user model
    user = User.objects.create(
        username=username,
        email=email,
        first_name=firstname,
        last_name=lastname
    )
    user.set_password(password)
    user.save()
    # create customer instance
    customer = Customer.objects.create(
        user=user,
        address=address,
        city=city,
        state=state,
        country=country,
        zipcode=zipcode,
        phone=phone
    )
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


def register_shop(request):
    return render(request, "register-shop.html")


def register_shop_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    cf_password = request.POST.get('cf-password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('lastname')
    shopname = request.POST.get('shopname')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    zipcode = request.POST.get('zipcode')
    description = request.POST.get('description')
    # validate
    if not validate_username(username):
        return render(request, "register-shop.html", {"msg": "Username already exist"})
    if not validate_password(password, cf_password):
        return render(request, "register-shop.html", {"msg": "Invalid password or confirm password"})
    if not validate_shop_name(shopname):
        return render(request, "register-shop.html", {"msg": "Shop name already exist"})
    # create base user model
    user = User.objects.create(
        username=username,
        email=email,
        first_name=firstname,
        last_name=lastname
    )
    user.set_password(password)
    user.save()
    # create customer instance
    shop = Shop.objects.create(
        owner=user,
        name=shopname,
        address=address,
        city=city,
        state=state,
        country=country,
        zipcode=zipcode,
        phone=phone,
        desc=description
    )
    return render(request, "login-shop.html", {"msg": "Completed registration"})


def validate_username(username):
    try:
        _ = User.objects.get(username=username)
    except User.DoesNotExist:
        return True
    return False


def validate_password(password, cf_password):
    return password == cf_password


def validate_shop_name(shopname):
    try:
        _ = Shop.objects.get(name=shopname)
    except Shop.DoesNotExist:
        return True
    return False
