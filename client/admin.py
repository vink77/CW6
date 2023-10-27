from django.contrib import admin

# Register your models here.
from django.contrib import admin
from client.models import Client, Message, Logs
from users.models import User
# Register your models here.
#admin.site.register(Category)

#admin.site.register(User)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_email','client_owner', 'client_comments',)
    list_filter = ('client_name',)
    search_fields = ('client_name', 'pk','client_owner',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'status', 'clients', 'theme', 'message_body')
    search_fields = ('period', 'status', 'clients')

    def clients(self, obj):
        return ', '.join([client.email for client in obj.mailing_clients.all()])

    clients.short_description = 'Message Clients'

@admin.register(Logs)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status', 'client')
    search_fields = ('last_try', 'status', 'client')