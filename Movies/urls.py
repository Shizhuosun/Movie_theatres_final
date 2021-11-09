from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.aboutus, name='aboutus'),
    path('movies', views.movies, name='movies'),
]

