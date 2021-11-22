from django import template
from django.conf import settings

register = template.Library()


def media_folder_products(string):
    if not string:
        string = 'product_images/i.webp'
    return f'{settings.MEDIA_URL}{string}'


@register.filter(name="medi_folder_users")
def media_folder_users(string):
    if not string:
        string = 'users_avatars/i.webp'
    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_products)
