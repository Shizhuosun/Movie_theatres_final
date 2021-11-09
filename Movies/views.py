from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Movie

def aboutus(request):
    return render(request, 'about-us/about-us.html')
    #return HttpResponse("Movie theatre")

def index(request):
    return HttpResponse("Movie theatre")


def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies_list': movies_list}
    return render(request, 'about-us/movies.html', context)