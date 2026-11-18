from django.contrib import admin
from .models import Personaje, EscuadronGremio, ArtefactoEquipamiento, Mision


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anime_origen', 'rango', 'habilidad_principal')
    search_fields = ('nombre', 'anime_origen')


@admin.register(EscuadronGremio)
class EscuadronGremioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capitan_lider', 'base_operaciones')


@admin.register(ArtefactoEquipamiento)
class ArtefactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'portador')


@admin.register(Mision)
class MisionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'rango_dificultad', 'escuadron_asignado', 'completada')
    list_filter = ('rango_dificultad', 'completada')
    