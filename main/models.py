from django.db import models

# Create your models here.

class Bajadery(models.Model):
    nazwa = models.CharField(max_length=150)
    ocena = models.FloatField()
    adres = models.URLField(default='-', blank=True)


