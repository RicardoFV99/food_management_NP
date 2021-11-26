# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: views.py
#
# Descripción:
#    El archivo contiene las vistas de la
#    aplicación de publicaciones, aquí se encuentra la
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

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import PublicacionCreateForm, PublicacionUpdateForm
from .models import Publicacion

from usuarios.models import Organizacion


class PublicacionCrear(PermissionRequiredMixin, CreateView):
	model = Publicacion
	form_class = PublicacionCreateForm
	permission_required = 'usuarios.crear_publicaciones'

	success_url = reverse_lazy('publicaciones:mis-publicaciones')

	extra_context = {
		'etiqueta': 'Crear',
		'boton': 'Publicar'
	}

	def form_valid(self, form):
		usuario = get_object_or_404(Organizacion, id=self.request.user.id)
		form.instance.usuario = usuario
		return super().form_valid(form)

@permission_required('usuarios.editar_publicaciones', raise_exception=True)
def mis_publicaciones(request):
	publicaciones = Publicacion.objects.all()

	publicaciones = publicaciones.filter(usuario=request.user.id)

	return render(request, 'publicaciones/publicacion_list.html', {'publicaciones': publicaciones})

@permission_required('usuarios.editar_publicaciones', raise_exception=True)
def publicacion_editar(request, pk):
	publicacion = get_object_or_404(Publicacion, id=pk)

	if not publicacion.usuario.id == request.user.id:
		return redirect('publicaciones:mis-publicaciones')

	form = PublicacionUpdateForm(instance=publicacion)
	if request.POST:
		form = PublicacionUpdateForm(request.POST, instance=publicacion)
		
		if form.is_valid():
			form.save()
			return redirect('publicaciones:mis-publicaciones')

	context = {
		'etiqueta': 'Editar',
		'boton': 'Guardar',
		'form': form,
	}
	
	return render(request, 'publicaciones/publicacion_form.html', context)

class PublicacionVer(LoginRequiredMixin, DetailView):
	model = Publicacion
	context_object_name = 'publicacion'

@permission_required('usuarios.eliminar_publicaciones', raise_exception=True)
def publicacion_eliminar(request, pk):
	publicacion = get_object_or_404(Publicacion, id=pk)
	
	if (publicacion.usuario.id == request.user.id):
		publicacion.delete()

	return redirect('publicaciones:mis-publicaciones')
	

# Copyright: Null Pointers 2021