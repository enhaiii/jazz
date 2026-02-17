from django.shortcuts import render, get_object_or_404
from .models import *

def start(request):
    context = {}
    return render(request, 'main.html', context)

def event(request):
    context = {}
    return render(request, 'events.html', context)

def online(request):
    context = {}
    return render(request, 'lives.html', context)

def live(request):
    context = {}
    return render(request, 'in_lives.html', context)

def formenu(request):
    context = {}
    return render(request, 'menu.html', context)

def forprofile(request):
    context = {}
    return render(request, 'profile.html', context)
