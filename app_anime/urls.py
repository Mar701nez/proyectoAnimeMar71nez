from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='login'),
    path('home/', views.home, name='home'),
    path('personajes/', views.personajes, name='personajes'),
    path('videos/', views.videos, name='videos'),
    path('musica/', views.musica, name='musica'),
    path('misiones/', views.misiones, name='misiones'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('salir/', views.cerrar_sesion, name='logout'),
    path('panel/', views.coleccion_mongo, name='coleccion_mongo'),
    path('eliminar/<str:anime_id>/', views.eliminar_anime, name='eliminar_anime'),
]