from django.contrib import admin

# Register your models here.
from django.contrib import admin
from client.models import Client
from users.models import User
# Register your models here.
#admin.site.register(Category)

#admin.site.register(User)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_email','client_owner', 'client_comments',)
    list_filter = ('client_name',)
    search_fields = ('client_name', 'pk','client_owner',)


