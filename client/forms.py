from django import forms

from client.models import Message


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class MessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'