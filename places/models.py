from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Описание', blank=True)
    description_long = HTMLField(verbose_name='Текст', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        unique_together = ('lng', 'lat')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    position = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name='Позиция',
    )
    place = models.ForeignKey(
        to=Place,
        on_delete=models.PROTECT,
        related_name='images',
        null=True,
        blank=True,
        verbose_name='Место',
    )

    class Meta:
        ordering = ('position', )
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        unique_together = (('image', 'place'), ('place', 'position'))

    def __str__(self):
        return f'#{self.position} {self.place}'
