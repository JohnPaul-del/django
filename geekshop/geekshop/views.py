from django.shortcuts import render
from mainapp.models import Product


header_menu = [
        {'href': '/', 'name': 'home'},
        {'href': '/products/', 'name': 'products'},
        {'href': '/contacts/', 'name': 'contacts'},
]


def main(request):
    title = "Shop"
    products = Product.objects.all()
    context = {
        'title': title,
        'header_menu': header_menu,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = "Contacts"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'geekshop/contact.html', context)
