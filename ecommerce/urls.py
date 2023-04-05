from django.urls import path
from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('products/search', views.search_products, name='search'),
    path('products/<str:category>', views.products, name='products'),
]