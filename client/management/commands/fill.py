from django.core.management.base import BaseCommand
import json
from catalog.models import Category, Product
class Command(BaseCommand):

    def handle(self, *args, **options):
#       print('Hi, Sky!')

        #Очищаем БД

        Category.objects.all().delete()
        Product.objects.all().delete()


#        categories = [
#            {'category_name': 'Пылесос', 'description': 'хорошо сосёт'},
#            {'category_name': 'Телевизор', 'description': 'хорошо показывает новости'},
#            {'category_name': 'Смартфон', 'description': 'хорошо звонят'},
#            {'category_name': 'Холодильник', 'description': 'хорошо морозят'},
#            {'category_name': 'Принтер', 'description': 'хорошо печатают'},
#            {'category_name': 'микроволновая печь', 'description': 'хорошо сосут'},
#
#        ]

        with open('catalog/data_json/data_users.json', 'r', encoding='UTF-8') as cat:
            category_to_fill = json.load(cat)
            for item in category_to_fill:
                Category.objects.create(
                    pk=item['pk'],
                    category_name=item['fields']['category_name'],
                    description=item['fields']['description']
                )
        with open('catalog/data_json/data_client.json', 'r', encoding='UTF-8') as prod:
            product_to_fill = json.load(prod)
            for item in product_to_fill:
                cat = Category.objects.get(pk=item['fields']['category'])
                Product.objects.create(
                    pk=item['pk'],
                    product_name=item['fields']['product_name'],
                    product_description = item['fields']['product_description'],
                    avatar=item['fields']['avatar'],
                    category=cat,
                    price=item['fields']['price'],
                    quantity_product=item['fields']['quantity_product'],
                    date_create = item['fields']['date_create'],
                    date_last_change=item['fields']['date_last_change'],
                )




#        category_to_fill = []
#        for category in categories:
#            category_to_fill.append(Category(**category))
#
#
#        # Пакетное заполнение БД
#
#        Category.objects.bulk_create(category_to_fill)