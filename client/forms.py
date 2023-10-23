from django import forms
from django.http import request

from client.models import Client, Message, Logs
from users.models import User


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class MessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Client
        print(User.objects.is_superuser)
        #if request.user.is_superuser:
        #    exclude = ['client_owner',]
        if User.get("is_superuser") is not True:





class SetMessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


class LogMessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Logs
        fields = '__all__'


class UserForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'