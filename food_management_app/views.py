from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Usuario, Organizacion, Publicacion
from .forms import UsuarioForm, OrganizacionForm, OrganizacionFormSignup, PublicacionForm


def landing_page(request):
	return render(request, 'landing_page.html', {})

def home(request):
	publicaciones = Publicacion.objects.all()

	return render(request, 'home.html', {'publicaciones': publicaciones})

class Login(LoginView):
	model = Organizacion
	template_name = 'login.html'

class Signin(CreateView):
	template_name = 'signin.html'
	form_class = OrganizacionFormSignup
	success_url = reverse_lazy('login')

class UpdatePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('logout')
	template_name = 'food_management_app/change-password.html'


#############################
#          USUARIO          #
#############################


class UsuarioVer(DetailView):
	model = Usuario

class UsuarioEditar(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	success_url = reverse_lazy('home')

class UsuarioEliminar(DeleteView):
	model = Usuario
	success_url = reverse_lazy('landing_page')


#############################
#        ORGANIZACIÓN       #
#############################


class OrganizacionVer(DetailView):
	model = Organizacion

class OrganizacionEditar(UpdateView):
	model = Organizacion
	form_class = OrganizacionForm
	success_url = reverse_lazy('landing_page')

class OrganizacionEliminar(DeleteView):
	model = Organizacion
	success_url = reverse_lazy('logout')


#############################
#        PUBLICACION        #
#############################


class PublicacionNueva(CreateView):
	model = Publicacion
	form_class = PublicacionForm
	success_url = reverse_lazy('home')

class PublicacionEditar(UpdateView):
	model = Publicacion
	form_class = PublicacionForm
	success_url = reverse_lazy('home')

class PublicacionEliminar(DeleteView):
	model = Publicacion
	success_url = reverse_lazy('home')

# Copyright: Null Pointers 2021