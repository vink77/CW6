from random import random

from django.shortcuts import render
from django.views.generic import ListView, UpdateView

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
