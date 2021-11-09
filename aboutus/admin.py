from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie,Actor
from .models import Question
# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Question)

class Movieadmin(admin.ModelAdmin):
    list_display = ("Name", "Price", "Duration", "Grade", "image",'booking_url')

class Actoradmin(admin.ModelAdmin):
    list_display = ("Name", "Gender" ,"Representative","Grade","image",'image_url')