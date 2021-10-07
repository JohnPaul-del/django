from django.shortcuts import render


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
        'links_menu': links_menu,
    }
    return render(request, "mainapp/products.html", context)
