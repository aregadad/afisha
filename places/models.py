from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Описание', blank=True)
    description_long = HTMLField(verbose_name='Текст', blank=True)
    custom_id = models.CharField(max_length=25, verbose_name='Кастомный ID', blank=True)
    lng = models.FloatField(verbose_name='Долгота', blank=True, null=True)
    lat = models.FloatField(verbose_name='Широта', blank=True, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.PositiveIntegerField(default=0, db_index=True)
    place = models.ForeignKey(Place, models.PROTECT, related_name='images', null=True, blank=True, verbose_name='Место')

    def __str__(self):
        return f'#{self.position} {self.place}'

    class Meta:
        ordering = ('position', )
