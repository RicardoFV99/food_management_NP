from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

from .models import Usuario, Organizacion, Publicacion
from .forms import UsuarioForm, OrganizacionForm, OrganizacionFormSignup, PublicacionForm

def landing_page(request):
    return render(request, 'landing_page.html', {})

def home(request):
    return render(request, 'home.html', {})

#############################
#          USUARIO          #
#############################


class Lista_usuarios(ListView):
    paginate_by = 4
    model = Usuario

class Eliminar_usuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario:lista')

class Nuevo_usuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nueva', 'boton':'Agregar', 'vj_nuevo':True}
    success_url = reverse_lazy('usuario:lista')

class Editar_usuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('usuario:lista')


#############################
#        ORGANIZACIÓN       #
#############################


class Lista_organizaciones(ListView):
    paginate_by = 4
    model = Organizacion

class Eliminar_organizacion(DeleteView):
    model = Organizacion
    success_url = reverse_lazy('organizacion:lista')

class Nueva_organizacion(CreateView):
    model = Organizacion
    form_class = OrganizacionForm
    extra_context = {'etiqueta':'Nueva', 'boton':'Agregar', 'vj_nuevo':True}
    success_url = reverse_lazy('organizacion:lista')

class Editar_organizacion(UpdateView):
    model = Organizacion
    form_class = OrganizacionForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('organizacion:lista')

class OrganizacionDetalle(DetailView):
    model = Organizacion

class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('logout')
    template_name = 'food_management_app/change-password.html'

#############################
#        PUBLICACION        #
#############################


class Lista_publicaciones(ListView):
    paginate_by = 4
    model = Publicacion

class Eliminar_publicacion(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicacion:lista')

class Nueva_publicacion(CreateView):
    model = Publicacion
    form_class = PublicacionForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'vj_nuevo':True}
    success_url = reverse_lazy('publicacion:lista')

class Editar_publicacion(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('publicacion:lista')

class Login(LoginView):
    model = Organizacion
    template_name = 'login.html'
    #form_class = AuthenticationForm
    #success_url = reverse_lazy('organizacion:lista')

class SignupOrganizacion(CreateView):
    template_name = 'signup.html'
    form_class = OrganizacionFormSignup
    success_url = reverse_lazy('log_in')

class EditarPerfil(UpdateView):
    model = Organizacion
    form_class = OrganizacionFormSignup
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('organizacion:lista')



# Copyright: Null Pointers 2021