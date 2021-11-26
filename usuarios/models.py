# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: models.py
#
# Descripción:
#    El archivo contiene las declaraciones de los
#    modelos de la aplicación de usuarios para así
#    utilizarlos en el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User._meta.get_field('first_name').blank = False
User._meta.get_field('first_name').null = False

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Donador(User):
	codigo_postal = models.IntegerField('Código Postal', validators=[MaxValueValidator(100000), MinValueValidator(0)])

	def __str__(self) -> str:
		return self.username


class Organizacion(Donador):
	direccion = models.CharField('Dirección', max_length=255)
	telefono = models.IntegerField('Teléfono')
	pagina_web = models.CharField('Página Web', max_length=255, blank=True, null=True)
	visibilidad = models.BooleanField('Visibilidad', default=True)

# Copyright: Null Pointers 2021