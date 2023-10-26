from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from client.views import ClientListView, ClientDeleteView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    LogDeleteView, LogListView
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


    #path('messages_menu', get_messages, name='messages_menu'),
    path('message_list',                 MessageListView.as_view(), name='message_list'),
    path('message/detail/<int:pk>',  MessageDetailView.as_view(), name='message_view'),
    path('message_create/',          MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('log/delete/<int:pk>/', LogDeleteView.as_view(), name='log_delete'),
    path('log_list/',             LogListView.as_view(), name='log_list'),



                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)