from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng_coord = models.FloatField()
    lat_coord = models.FloatField()

    def __str__(self):
        return self.title
