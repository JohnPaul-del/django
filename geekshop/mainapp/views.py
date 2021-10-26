import random
from django.shortcuts import render, get_object_or_404
from geekshop.views import header_menu
from .models import ProductCategory, Product
from basketapp.models import Basket


def products(request, pk=None):
    title = 'Catalog'
    links_menu = ProductCategory.objects.all()
    _products = Product.objects.all().order_by('price')
    basket = get_basket(request.user)
    if pk is not None:
        if pk == 0:
            _products = Product.objects.order_by('price')
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            _products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'header_menu': header_menu,
            'links_menu': links_menu,
            'category': category,
            'products': _products,
            'basket': basket,
        }
        return render(request, "mainapp/products.html", context)

    hot_product = get_hot_product()
    same_products = Product.objects.all()[1:2]
    context = {
        'title': title,
        'header_menu': header_menu,
        'hot_product': hot_product,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
    }
    return render(request, "mainapp/products.html", context)


def product(request, pk):
    title = 'More'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': product,
        'same_products': get_same_products(product),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', context)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:1]
    return same_products


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]
