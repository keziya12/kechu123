from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Movie


def fun(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "index.html", context)


def fun2(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "bye.html", {'movie': movie})

# re turn HttpResponse("welcome %s" % movie_id)
