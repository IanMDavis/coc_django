from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Character
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def character(request):
    context = {'characters':Character.objects.all()}
    return render(request, 'character.html', context)

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = User.objects.create_user(username=username, password=password)

        return render(request, 'index.html')

    else:
        return render(request, 'create_user.html')