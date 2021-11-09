from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from . import models

#app_name = 'polls'

urlpatterns = [
    path('', views.aboutus),
    path('base', views.base, name='base'),
    path('', views.aboutus, name='aboutus'),
    path('movies',views.movies, name='movies'),
    path('actors',views.actors, name='actors'),
    path('start',views.start, name='start'),
    #path('info',views.info, name='info'),

    #path('search',views.search, name='search'),
    path(r'search/', views.search),

    path('polls',views.polls, name='polls'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

