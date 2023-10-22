import os

from django.core.management.base import BaseCommand
import json
from client.models import Client
from config import settings
from users.models import User
class Command(BaseCommand):

    def handle(self, *args, **options):
#       print('Hi, Sky!')

        #Очищаем БД

        Client.objects.all().delete()
        User.objects.all().delete()



#

        with open('client/data_json/data_users.json', 'r', encoding='UTF-8') as us:
            users_to_fill = json.load(us)
            for item in users_to_fill:
                User.objects.create(
                    #pk=item['pk'],
                    email=item['fields']['email'],
                    phone=item['fields']['phone'],
                    avatar=item['fields']['avatar'],
                    is_staff=True,
                    is_superuser=True,
                )


        with open('client/data_json/data_client.json', 'r', encoding='UTF-8') as cl:
            client_to_fill = json.load(cl)
            for item in client_to_fill:
                print(item)
                print(item['fields']['client_name'])
                owner_user = User.objects.get(pk=item['fields']['owner'])
                Client.objects.create(
                    #pk=item['pk'],
                    client_name=item['fields']['client_name'],
                    client_email=item['fields']['client_email'],
                    client_comments=item['fields']['client_comments'],
                    client_owner=owner_user,

                )

#        user = User.objects.create(
#            email=settings.EMAIL_HOST_USER,
#            first_name='Admin',
#            last_name='SkyPro',
#            is_staff=True,
#            is_superuser=True,
#        )
#        user.set_password(os.getenv('DATABASE_PASSWORD'))
#        user.save()


#        category_to_fill = []
#        for category in categories:
#            category_to_fill.append(Category(**category))
#
#
#        # Пакетное заполнение БД
#
#        Category.objects.bulk_create(category_to_fill)