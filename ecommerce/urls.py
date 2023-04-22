from django.urls import path
from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('', views.home, name='home'),
    # auth
    path('login', views.login_customer, name='login'),
    path('login/submit', views.login_customer_submit, name='login-submit'),
    path('logout', views.logout_customer, name='logout'),
    path('register', views.register_custemer, name='register'),
    path('register/submit', views.register_customer_submit, name='register-submit'),
    # customer
    path('customer/profile/<int:customer_id>', views.customer_profile, name="customer-profile"),
    path('customer/profile/<int:customer_id>/edit-profile', views.customer_edit, name="customer-edit"),
    path('customer/profile/<int:customer_id>/edit-profile/submit', views.edit_customer_profile_submit, name="edit-customer-profile-submit"),
    path('customer/profile/<int:customer_id>/remove-cart-item/<int:cart_item_id>', views.remove_cart_item, name="remove-cart-item"),
    path('customer/profiel/<int:customer_id>/order/create', views.create_order, name='create-order'),
    # products
    path('products/search', views.search_products, name='search'),
    path('products/<str:category>', views.products, name='products'),
    path('product-detail/<int:product_id>', views.product_detail, name='product-detail'),
    path('product-detail/<int:product_id>/add-to-cart/<int:customer_id>', views.add_to_cart, name='add-to-cart'),
    # shop
    path('shop/login', views.login_shop, name='login-shop'),
    path('shop/login/submit', views.login_shop_submit, name='login-shop-submit'),
    path('shop/register', views.register_shop, name="register-shop"),
    path('shop/register/submit', views.register_shop_submit, name="register-shop-submit"),
    path('shop/<int:shop_id>', views.shop, name="shop"),
    path('shop/profile/<int:shop_id>', views.shop_profile, name="shop-profile"),
    path('shop/profile/<int:shop_id>/delete-item/<int:item_id>', views.delete_item, name="delete-item"),
    path('shop/profile/<int:shop_id>/shop-add', views.shop_add, name="shop-add"),
    path('shop/profile/<int:shop_id>/shop-add/submit', views.add_item_shop_submit, name="add-item-shop-submit"),
    path('shop/profile/<int:shop_id>/edit-profile', views.shop_edit, name="shop-edit"),
    path('shop/profile/<int:shop_id>/edit-profile/submit', views.edit_shop_profile_submit, name="edit-shop-profile-submit"),
    path('shop/profile/<int:shop_id>/order', views.shop_order, name="shop-order"),
]