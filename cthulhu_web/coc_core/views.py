from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Character

def index(request):
    return render(request, "index.html")

def character(request):
    context = {"characters":Character.objects.all()}
    return render(request, "character.html", context)