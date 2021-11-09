from django.conf.urls import url,include
from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    #path('', views.aboutus, name='aboutus'),
    path('login', views.login, name='login'),
    path('logindex', views.logindex, name='logindex'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]