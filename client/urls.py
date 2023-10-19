from django.urls import path
from django.conf import settings
from client.views import client_list, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView
from client.apps import ClientConfig


app_name = ClientConfig.name

#urlpatterns = [path('', ClientListView.as_view(), name='list'),  # Домашняя страница
#               ]





urlpatterns = [
    path('', ClientListView.as_view(), name='list'),  # Домашняя страница
    path('create/', ClientCreateView.as_view(), name='create'),  # Домашняя страница
    path('view/<int:pk>/', ClientDetailView.as_view(), name='view'),  # Домашняя страница
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),  # Домашняя страница

]