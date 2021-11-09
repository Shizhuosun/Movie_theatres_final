
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.CharField(max_length=10)
    grade = models.FloatField()
    image_url = models.CharField(max_length=2083)
    booking_url = models.CharField(max_length=2083)



class Actor(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    representative =models.CharField(max_length=2083)
    grade = models.FloatField()
    image = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    #booking_url = models.CharField(max_length=2083)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text