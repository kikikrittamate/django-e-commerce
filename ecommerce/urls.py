from django.urls import path
from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('', views.home, name='home'),
    # customer
    path('login', views.login_customer, name='login'),
    path('login/submit', views.login_customer_submit, name='login-submit'),
    path('logout', views.logout_customer, name='logout'),
    path('register', views.register_custemer, name='register'),
    path('register/submit', views.register_customer_submit, name='register-submit'),
    # products
    path('products/search', views.search_products, name='search'),
    path('products/<str:category>', views.products, name='products'),
    path('product-detail/<int:product_id>', views.product_detail, name='product-detail'),
    # shop
    path('shop/profile/<int:shop_id>', views.shop_profile, name="shop-profile"),
    path('shop/login', views.login_shop, name='login-shop'),
    path('shop/login/submit', views.login_shop_submit, name='login-shop-submit'),
    path('shop/<int:shop_id>', views.shop, name="shop"),
]