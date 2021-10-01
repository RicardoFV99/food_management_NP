from django.shortcuts import render, redirect
from .models import Organizacion
from .models import Publicacion
from .models import Usuario
from .forms import OrganizacionForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings


class Lista_organizaciones(ListView):
    paginate_by = 4
    model = Organizacion

class Eliminar_organizacion(DeleteView):
    model = Organizacion
    success_url = reverse_lazy('organizacion:lista')

class Nueva_organizacion(CreateView):
    model = Organizacion
    form_class = OrganizacionForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'vj_nuevo':True}
    success_url = reverse_lazy('organizacion:lista')

class Editar_organizacion(UpdateView):
    model = Organizacion
    form_class = OrganizacionForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar'}
    success_url = reverse_lazy('organizacion:lista')

# Create your views here.
