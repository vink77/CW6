from django.urls import path
from django.conf import settings
from client.views import ClientListView
from client.apps import ClientConfig


app_name = ClientConfig.name

urlpatterns = [path('', ClientListView.as_view(), name='list'),  # Домашняя страница
               ]