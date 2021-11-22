from django.core.management.base import BaseCommand
import json, os
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

JSON_PATH = 'mainapp/jsons'


def load_json_data(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as datafile:
        return json.load(datafile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_json_data('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_json_data('products')
        Product.objects.all().delete()
        for product in products:
            product_category = product['category']
            _category = ProductCategory.objects.get(name=product_category)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # super_user = ShopUser.objects.create_superuser('admin', 'test@test.com', '321', age=44)
        # if super_user:
        #     print("Created")
