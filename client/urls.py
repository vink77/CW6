from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from client.views import ClientListView, ClientDeleteView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    get_messages
from client.apps import ClientConfig


app_name = ClientConfig.name

#urlpatterns = [path('', ClientListView.as_view(), name='list'),  # Домашняя страница
#               ]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('client_list/', ClientListView.as_view(), name='client_list'),  # Домашняя страница
    path('create/', ClientCreateView.as_view(), name='create'),  # Домашняя страница
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='detail'),  # Домашняя страница
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='view'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),


    path('messages_menu', get_messages, name='messages_menu'),
    path('messages', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_item'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)