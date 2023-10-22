from django.db import models
from datetime import datetime

from django.utils.text import slugify

NULLABLE = {"null": True, "blank": True}

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    conteхt = models.TextField(verbose_name='Содержимое')
    preview_img = models.ImageField(upload_to='blog/images/', verbose_name='Превью(изображение)', **NULLABLE)
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    date_create = models.DateField(verbose_name='Дата создания', default=current_time)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)

    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f'{self.title}'


class Meta:
    verbose_name = 'блог'
    verbose_name_plural = 'блога'
    ordering = ('title',)

