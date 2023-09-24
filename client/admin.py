from django.contrib import admin

# Register your models here.
from django.contrib import admin
from client.models import Client
from users.models import Users
# Register your models here.
#admin.site.register(Category)

#admin.site.register(Product)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client_name', 'client_comments',)
    list_filter = ('client_name',)
    search_fields = ('client_name', 'pk',)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_name',)
    list_filter = ('user_name',)