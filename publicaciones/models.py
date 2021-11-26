# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: models.py
#
# Descripción:
#    El archivo contiene las declaraciones de los
#    modelos de la aplicación de publicaciones para
#    utilizarlos en el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.db import models

class Publicacion(models.Model):
	usuario = models.ForeignKey('usuarios.Organizacion', blank=True, null=True, verbose_name='Organización', on_delete=models.CASCADE)
	contenido = models.TextField('Contenido', max_length=255)
	fecha_hora_publicacion = models.DateTimeField(auto_now=True, editable=False)

# Copyright: Null Pointers 2021