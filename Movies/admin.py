from django.contrib import admin
from .models import Movie
# Register your models here.
admin.site.register(Movie)

class Movieadmin(admin.ModelAdmin):
    list_display = ("Name", "Price", "Duration", "Grade", "image")