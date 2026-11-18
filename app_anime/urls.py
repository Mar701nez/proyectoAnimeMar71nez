from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personajes/', views.personajes, name='personajes'),
    path('videos/', views.videos, name='videos'),
    path('musica/', views.musica, name='musica'),
    path('misiones/', views.misiones, name='misiones'),
]