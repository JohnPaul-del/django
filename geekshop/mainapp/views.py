from django.shortcuts import render
from geekshop.views import header_menu
from .models import ProductCategory, Product


def products(request, pk=None):
    title = 'Catalog'
    links_menu = ProductCategory.objects.all()[:6]
    print(pk)
    context = {
        'title': title,
        'header_menu': header_menu,
        'links_menu': links_menu,
    }
    return render(request, "mainapp/products.html", context)
