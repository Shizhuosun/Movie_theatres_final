from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.CharField(max_length=10)
    grade = models.FloatField()
    image_url = models.CharField(max_length=2083)