from django.shortcuts import render

header_menu = [
    {'full_name': 'mainapp:main','app_name': 'mainapp', 'url_name': 'main', 'name': 'home'},
    {'full_name': 'mainapp:products','app_name': 'mainapp', 'url_name': 'products', 'name': 'products'},
    {'full_name': 'mainapp:contacts','app_name': 'mainapp', 'url_name': 'contacts', 'name': 'contacts'},
]


def main(request):
    title = "Shop"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    title = "Contacts"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'mainapp/contact.html', context)


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
