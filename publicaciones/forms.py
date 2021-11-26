# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: forms.py
#
# Descripción:
#    El archivo contiene las declaraciones de los
#    formularios de la aplicación de publicaciones 
#    para utilizarlos en las vistas que los requieran.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django import forms
from django.forms import widgets

from .models import Publicacion

class PublicacionCreateForm(forms.ModelForm):

	class Meta:
		model = Publicacion

		fields = ('usuario', 'contenido')

		widgets = {
			'usuario': forms.Select(attrs={'disabled': True, 'hidden': True}),
			'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación...'})
		}

		labels = {
			'usuario': '',
			'contenido': ''
		}

class PublicacionUpdateForm(forms.ModelForm):

	class Meta:
		model = Publicacion

		fields = ('contenido', )

		widgets = {
			'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación...'})
		}

		labels = {
			'contenido': ''
		}

# Copyright: Null Pointers 2021