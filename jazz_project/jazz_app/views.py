from django.shortcuts import render, get_object_or_404
from .models import *

def start(request):
    context = {}
    return render(request, 'main.html', context)

def event(request):
    context = {}
    return render(request, 'events.html', context)
