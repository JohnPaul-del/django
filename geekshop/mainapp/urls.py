from django.urls import path
from .views import main, contacts, products

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
]
