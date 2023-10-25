from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

import client
from client.forms import MessageForm, ClientForm
from client.models import Client, Message, Logs


# Create your views here.
def home(request):
    """Домашняя страница с выводом списка всех созданных, но не проведенных рассылок"""

    return render(request, 'client/base.html')

#def client_list(request):
#    """Домашняя страница с выводом списка всех созданных, но не проведенных рассылок"""
#
#    return render(request, 'client/client_list.html')

#class ClientListView(ListView):
#    model = Client
 #   context_object_name = 'client'

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'

    def get_queryset(self):
        """Фильтр на отображение только клиентов пользователя"""
        user = self.request.user

        if  user.is_superuser:
            queryset = Client.objects.all()
        else:
            queryset = Client.objects.filter(client_owner=user)
        return queryset


class ClientCreateView(CreateView):
    model = Client
    # fields = ('product_name', 'product_description')
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.client_owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())



class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')




class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер страницы рассылок"""
    model = Message
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self):
        """Фильтр на отображение только клиентов пользователя"""
        # queryset = super().get_queryset()

        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Message.objects.all()
        else:
            queryset = Message.objects.filter(client_owner=user)

        #queryset = queryset.filter(is_publication=True)
        return queryset

class MessageDetailView(DetailView):
    """Контроллер постраничного вывода информации о рассылках"""
    model = Message

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('client:message_list')

    def form_valid(self, form):
        """Привязка создаваемого рассылки к авторизованному пользователю"""
        form.instance.User = self.request.user
        return super(MessageCreateView, self).form_valid(form)



class MessageUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Контроллер изменения рассылки"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('client:message_list')

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client:message_detail', args=[self.object.pk])


class MessageDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Контроллер удаления рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')

def get_messages(request):
    """Контроллер меню рассылки"""
    context = {
        'title': 'Меню рассылки'
    }
    return render(request, 'client/messages_menu.html', context)

def messages_logs(request, mailing_id):
    mailing = get_object_or_404(Message, pk=mailing_id)
    logs = Logs.objects.filter(log_mailing=mailing).order_by('-created_time')

    if (mailing.owner == request.user or request.user.is_superuser
            or request.user.groups.filter(name='manager').exists()):
        context = {
            'mailing': mailing,
            'logs': logs,
        }
        return render(request, 'client/messages_logs.html', context)
    else:
        return redirect("client:message_list")