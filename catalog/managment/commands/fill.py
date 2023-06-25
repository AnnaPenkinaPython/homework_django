from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


def read_category_data_json():
    with open('category_data.json') as file:
        category_data = json.load(file)
    return category_data


def read_products_data_json():
    with open('products_data.json') as file:
        products_data = json.load(file)
    return products_data


class Command(BaseCommand):
    def handle(self, *args, options):
        category = []
        products = []
        category_list = read_category_data_json()
        product_list = read_products_data_json()

        for category_item in category_list:
            category.append(Category(category_item))
        Category.objects.bulk_create(category)
        for product_item in product_list:
            products.append(Product(**product_item))
        Product.objects.bulk_create(products)
    print('Данные успешно заполнены!')