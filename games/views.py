from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def index(request):
    context = {}
    return render(request, 'home_game.html', context)

