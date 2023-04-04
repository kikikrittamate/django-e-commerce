from django.urls import path
from . import views

app_name = 'ecommerce'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('products/<str:category>', views.products, name='products'),
]