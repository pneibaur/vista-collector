from django.shortcuts import render
from django.http import HttpResponse
from vistas_collector.models import Vista

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vistas_index(request):
    vistas = Vista.objects.all()
    return render(request, "vistas/index.html", {"vistas": vistas})