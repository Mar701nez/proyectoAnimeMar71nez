from django.db import models


class Personaje(models.Model):
    OPCIONES_ANIME = [
        ('Black Clover', 'Black Clover'),
        ('Kimetsu no Yaiba', 'Kimetsu no Yaiba'),
        ('Kakashi', 'Kakashi Chronicles / Naruto'),
    ]

    nombre = models.CharField(max_length=100)
    anime_origen = models.CharField(max_length=50, choices=OPCIONES_ANIME)
    rango = models.CharField(max_length=50, help_text="Ej: Caballero Mágico, Pilar, Jōnin")
    habilidad_principal = models.CharField(max_length=100, help_text="Ej: Anti-Magia, Raikiri, Respiración del Sol")

    def __str__(self):
        return f"{self.nombre} ({self.anime_origen})"


class EscuadronGremio(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Toros Negros, Cazadores de Demonios, ANBU
    capitan_lider = models.CharField(max_length=100)  # Ej: Yami Sukehiro, Kagaya, Kakashi
    base_operaciones = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class ArtefactoEquipamiento(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Grimorio 5 Tréboles, Katana Nichirin
    tipo = models.CharField(max_length=50)  # Ej: Espada, Pergamimo, Máscara
    portador = models.ForeignKey(Personaje, on_delete=models.CASCADE, related_name='artefactos')

    def __str__(self):
        return f"{self.nombre} - Portador: {self.portador.nombre}"


class Mision(models.Model):
    OPCIONES_DIFICULTAD = [
        ('Rango S', 'Rango S'),
        ('Rango A', 'Rango A'),
        ('Rango B', 'Rango B'),
    ]

    titulo = models.CharField(max_length=150)
    rango_dificultad = models.CharField(max_length=20, choices=OPCIONES_DIFICULTAD)
    escuadron_asignado = models.ForeignKey(EscuadronGremio, on_delete=models.CASCADE, related_name='misiones')
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} [{self.rango_dificultad}]"