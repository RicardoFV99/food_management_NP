# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: views.py
#
# Descripción:
#    El archivo contiene las vistas de la
#    aplicación de usuarios, aquí se encuentra la
#    lógica que es necesaria al momento de interactuar
#    con el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import CambiarContrasenaForm, DonadorUpdateForm, OrganizacionUpdateForm
from .models import Donador, Organizacion


class CambiarContrasena(LoginRequiredMixin, UpdateView):
	model = Donador
	form_class = CambiarContrasenaForm
	template_name = 'usuarios/change_password.html'
	success_url = reverse_lazy('home:home')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		donador = Donador.objects.get(username=pk)
		return donador



#############################
#          USUARIO          #
#############################


class DonadorPerfil(LoginRequiredMixin, DetailView):
	model = Donador
	context_object_name = 'donador'

	def get_object(self, queryset=None):
		pk = self.request.user.username
		donador = Donador.objects.get(username=pk)
		return donador

class DonadorEditarPerfil(LoginRequiredMixin, UpdateView):
	model = Donador
	form_class = DonadorUpdateForm

	success_url = reverse_lazy('usuarios:mi-perfil')

	extra_context = {
		'etiqueta': 'Actualizar',
		'boton': 'Guardar'
	}

	def get_object(self, queryset=None):
		pk = self.request.user.username
		donador = Donador.objects.get(username=pk)
		return donador
	
class DonadorEliminar(LoginRequiredMixin, DeleteView):
	model = Donador
	success_url = reverse_lazy('home:landing_page')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		donador = Donador.objects.get(username=pk)
		return donador


#############################
#        ORGANIZACIÓN       #
#############################


class OrganizacionVer(LoginRequiredMixin, DetailView):
	model = Organizacion
	context_object_name = 'organizacion'

class OrganizacionPerfil(LoginRequiredMixin, DetailView):
	model = Organizacion
	context_object_name = 'organizacion'
	template_name = 'usuarios/organizacion_perfil.html'

	def get_object(self, queryset=None):
		pk = self.request.user.username
		organizacion = Organizacion.objects.get(username=pk)
		return organizacion

class OrganizacionEditarPerfil(LoginRequiredMixin, UpdateView):
	model = Organizacion
	form_class = OrganizacionUpdateForm

	success_url = reverse_lazy('usuarios:organizacion-mi-perfil')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		organizacion = Organizacion.objects.get(username=pk)
		return organizacion

class OrganizacionEliminar(LoginRequiredMixin, DeleteView):
	model = Organizacion
	success_url = reverse_lazy('home:landing_page')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		organizacion = Organizacion.objects.get(username=pk)
		return organizacion

# Copyright: Null Pointers 2021