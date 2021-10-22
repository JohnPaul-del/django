from django.shortcuts import render, get_object_or_404
from geekshop.views import header_menu
from .models import ProductCategory, Product


def products(request, pk=None):
    title = 'Catalog'
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')
    if pk is not None:
        if pk == 0:
            products = Product.objects.order_by('price')
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'header_menu': header_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }
        return render(request, "mainapp/products.html", context)

    same_products = Product.objects.all()[1:2]
    context = {
        'title': title,
        'header_menu': header_menu,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
    }
    return render(request, "mainapp/products.html", context)

