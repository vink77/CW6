from random import random

from django.shortcuts import render
from django.views.generic import ListView, UpdateView

import client
from client.models import Mailing, Client


# Create your views here.
def home(request):
    """Домашняя страница с выводом списка всех созданных, но не проведенных рассылок"""

    return render(request, 'client/home.html')

def client_list(request):
    """Домашняя страница с выводом списка всех созданных, но не проведенных рассылок"""

    return render(request, 'client/client_list.html')

#class ClientListView(ListView):
#    model = Client
 #   context_object_name = 'client'

class ClientUpdateView(UpdateView):
    model = Client

class ClientListView(ListView):
    model = client
    template_name = 'catalog/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = client.objects.all()
        categories = get_categories()
        for product in products:
            product.active_version = product.versions.filter(is_active=True).first()
        context['products'] = products
        context['categories'] = categories
        return context
