from django.shortcuts import render, redirect
from django.urls import reverse
from ecommerce.models import Customer, Shop, Item , Cart,  CartItems
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def customer_profile(request, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    try:
        customer = Customer.objects.get(user_id=customer_id)
    except:
        return render(request, 'error/404.html')
    cart = Cart.objects.filter(is_ordered=False, customer = customer )
    context = { 'customer': customer }
    return render(request, 'customer-profile.html', context )


@login_required(login_url="/login")
def customer_edit(request, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    customer=Customer.objects.get(user_id=customer_id)
    return render(request, 'edit-customer-profile.html', { 'customer': customer})


@login_required(login_url="/login")
def edit_customer_profile_submit(request, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    customer=Customer.objects.get(user_id=customer_id)
    if request.method == "POST":
        customer.user.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.address = request.POST.get('address')
        customer.city = request.POST.get('city')
        customer.state = request.POST.get('state')
        customer.country = request.POST.get('country')
        customer.zipcode = request.POST.get('zipcode')
        customer.img = request.POST.get('img')
        customer.save()
        customer.user.save()
    context={ 'customer': customer }
    return redirect(reverse("ecommerce:customer-profile", kwargs={"customer_id": customer.user_id}), context)

@login_required(login_url="/login")
def add_to_cart(request, product_id, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    item = Item.objects.get(id=product_id, is_deleted=False)
    customer = Customer.objects.get(id=customer_id)
    cart , _ = Cart.objects.get_or_create(customer=customer, is_paid=False)
    cart_items = CartItems.object.create(cart=cart,item=item)
    context = { 'cart': cart, 'cart-items': cart_items }
    return redirect(reverse("ecommerce:customer-profile", kwargs={"customer_id": customer.user_id}), context)

@login_required(login_url="/login")
def item_in_cart(request, product_id, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    item = Item.objects.get(id=product_id, is_deleted=False)
    customer = Customer.objects.get(id=customer_id)
    cart , _ = Cart.objects.get_or_create(customer=customer, is_paid=False)
    cart_items = CartItems.object.get(cart=cart,item=item)
    context = { 'cart': cart, 'item-in-cart' : cart_items  }
    return render(request, 'customer-profile.html', context)


@login_required(login_url="/login")
def remove_cart_item(request, customer_id, cart_item_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    cart_items = CartItems.object.get(id=cart_item_id)
    cart_items.delete()
    customer=Customer.objects.get(user_id=customer_id)
    return redirect(reverse("ecommerce:customer-profile", kwargs={"customer_id": customer.user_id}))