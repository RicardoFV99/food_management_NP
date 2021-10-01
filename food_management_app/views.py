from django.shortcuts import render, redirect
from .models import Organizacion
from .models import Publicacion
from .models import Usuario
from .forms import OrganizacionForm
from .forms import PublicacionForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings

#ORGANIZACION

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

#PUBLICACION

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


# Create your views here.
