from django.db import models
from config import settings
from users.models import User

NULLABLE = {"null": True, "blank": True}

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='ФИО')
    client_email = models.EmailField(unique=True, verbose_name='почта')
    client_comments = models.TextField(**NULLABLE, verbose_name='комментарии')
    client_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец',**NULLABLE)

    def __str__(self):
        return f'{self.client_email} ({self.client_name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'



class Message(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )
    theme = models.CharField(max_length=250, verbose_name='Тема')
    message_body = models.TextField(verbose_name='Тело')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    #settings = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Настройка')

    time = models.TimeField(verbose_name='Время')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='Период')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='Статус')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.client} / {self.settings}'


class Logs(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    settings = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Настройка')

    status = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='Статус')

    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')


    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


