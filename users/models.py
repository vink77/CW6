from django.db import models
NULLABLE = {"null": True, "blank": True}

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='ФИО')
    user_email = models.EmailField(verbose_name='почта', unique=True)
    user_password = models.TextField(**NULLABLE)
    #owner = models.ForeignKey(on_delete=models.SET_NULL, **NULLABLE)  # Владелец (ссылка)

    def __str__(self):
        return f'{self.user_email} ({self.user_name})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'