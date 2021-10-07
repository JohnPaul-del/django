from django.shortcuts import render
from geekshop.views import header_menu


def products(request):
    title = 'Catalog'
    links_menu = [
        {'href': 'products', 'name': 'all'},
        {'href': 'products_home', 'name': 'home'},
        {'href': 'products_office', 'name': 'office'},
        {'href': 'products_classic', 'name': 'classic'},
    ]

    context = {
        'title': title,
        'header_menu': header_menu,
        'links_menu': links_menu,
    }
    return render(request, "mainapp/products.html", context)
