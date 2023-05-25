from django.db import models

# Create your models here.
class Painting(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    creation_year = models.IntegerField()

    def __str__(self):
        return f'{self.title} by {self.artist}'
