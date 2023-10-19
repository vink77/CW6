from django.db import models
from config import settings

NULLABLE = {"null": True, "blank": True}

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='ФИО')
    client_email = models.EmailField(unique=True, verbose_name='почта')
    client_comments = models.TextField(**NULLABLE, verbose_name='комментарии')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)  # User (ссылка)

    def __str__(self):
        return f'{self.client_email} ({self.client_name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'



class Mailing(models.Model):
    mailing_time = models.DateTimeField()
    period = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Message(models.Model):
    theme = models.CharField(max_length=150)
    message_body = models.TextField()

class Logs(models.Model):
    last_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    answer = models.TextField(**NULLABLE)



