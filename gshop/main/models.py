from django.db import models


class Poster(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=250)
    image = models.ImageField(upload_to='img/poster')

    def __str__(self):
        return self.title

    class Meta:
         verbose_name = 'Poster'
         verbose_name_plural = 'Posters'
# Create your models here.
