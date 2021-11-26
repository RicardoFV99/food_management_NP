# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: views.py
#
# Descripción:
#    El archivo contiene las vistas de la aplicación
#    home, aquí se encuentra la lógica de las vistas
#    que no son pertenecientes a modelos específicos.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from publicaciones.models import Publicacion
from usuarios.models import Donador
from usuarios.forms import DonadorCreateForm, OrganizacionCreateForm

def landing_page(request):
	if request.user.is_authenticated:
		return redirect('home:home')

	return render(request, 'landing_page.html')

@login_required
def home(request):
	publicaciones = Publicacion.objects.order_by('-fecha_hora_publicacion')

	return render(request, 'home.html', {'publicaciones': publicaciones})

class Login(LoginView):
	model = Donador
	template_name = 'login.html'

def signin(request):
	if request.user.is_authenticated:
		return redirect('home:home')

	if request.POST:
		print("POST")
		if request.POST.get("es_organizacion", None):
			print("Organizacion")
			form = OrganizacionCreateForm(request.POST)
		else:
			print("Usuario")
			form = DonadorCreateForm(request.POST)

		print(form.is_valid())

		if form.is_valid():
			print("Valid")
			form.save()
			return redirect('home:login')

	return render(request, 'signin.html', {})

# Copyright: Null Pointers 2021