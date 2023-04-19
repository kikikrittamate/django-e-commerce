from django.shortcuts import render, redirect
from django.urls import reverse
from ecommerce.models import Customer
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def customer_profile(request, customer_id):
    if request.user.id != customer_id:
        # msg: You are not customer
        return render(request, 'error/403.html', status=403)
    customer = Customer.objects.get(user_id=customer_id)
    return render(request, 'customer-profile.html', { 'customer': customer } )


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