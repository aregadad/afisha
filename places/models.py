from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng_coord = models.FloatField()
    lat_coord = models.FloatField()

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    position = models.IntegerField()
    place = models.ForeignKey(Place, models.PROTECT, related_name='images', null=True, blank=True)

    def __str__(self):
        return f'{self.position} {self.place}'