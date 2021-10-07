from django.shortcuts import render
header_menu = [
        {'href': '/', 'name': 'home'},
        {'href': '/products/', 'name': 'products'},
        {'href': '/contacts/', 'name': 'contacts'},
]


def main(request):
    title = "Shop"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = "Contacts"
    context = {
        'title': title,
        'header_menu': header_menu,
    }
    return render(request, 'geekshop/contact.html', context)
