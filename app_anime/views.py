from django.shortcuts import render
from .models import Personaje, EscuadronGremio, Mision


def home(request):
    return render(request, 'app_anime/home.html')


def personajes(request):
    personajes_list = Personaje.objects.all()
    escuadrones_list = EscuadronGremio.objects.all()
    context = {
        'personajes': personajes_list,
        'escuadrones': escuadrones_list,
    }
    return render(request, 'app_anime/personajes.html', context)


def videos(request):
    return render(request, 'app_anime/videos.html')


def musica(request):
    return render(request, 'app_anime/musica.html')


def misiones(request):
    misiones_list = Mision.objects.all()
    return render(request, 'app_anime/misiones.html', {'misiones': misiones_list})