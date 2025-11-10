# app_Netflix/admin.py
from django.contrib import admin
from .models import Usuario, Pelicula # Importa también Pelicula

admin.site.register(Usuario)
admin.site.register(Pelicula) # Registra el modelo Pelicula