from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import Log
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView

import client
from client.forms import MessageForm, ClientForm
from client.models import Client, Message, Logs
from users.models import User


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
            queryset = Message.objects.filter(owner=user)

        #queryset = queryset.filter(is_publication=True)
        return queryset

class MessageDetailView(DetailView):
    """Контроллер постраничного вывода информации о рассылках"""
    model = Message
    template_name = 'client/Message_detail.html'

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


class MessageDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Контроллер удаления рассылки"""
    model = Message
    success_url = reverse_lazy('mailing:message_list')

class LogListView(ListView):
    model = Logs
    template_name = 'client/log_list.html'

    def get_queryset(self):
        """Фильтр на отображение только отчетов пользователя"""
        user = self.request.user

        if user.is_superuser:
            queryset = Logs.objects.all()
        else:
            queryset = Logs.objects.filter(client_owner=user)
        return queryset


class LogDeleteView(DeleteView):
    model = Logs
    success_url = reverse_lazy('client:log_list')

