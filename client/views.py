from random import random

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, CreateView

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
    model = Client
    template_name = 'client/client_list.html'

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    Clients = client.objects.all()
    #    categories = get_categories()
    #    for client in Clients:
    #        client.active_version = client.versions.filter(is_active=True).first()
    #    context['products'] = products
    #    context['categories'] = categories
    #    return context

class ClientCreateView(CreateView):
    pass

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'

