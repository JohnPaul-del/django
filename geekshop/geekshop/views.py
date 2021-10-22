from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket


header_menu = [
        {'href': '/', 'name': 'home'},
        {'href': '/products/', 'name': 'products'},
        {'href': '/contacts/', 'name': 'contacts'},
]


def main(request):
    title = "Shop"
    basket = Basket.objects.filter(user=request.user)
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'header_menu': header_menu,
        'products': products,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = "Contacts"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'geekshop/contact.html', context)
