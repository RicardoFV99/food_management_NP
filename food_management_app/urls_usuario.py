from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
	path('ver/<int:pk>', views.UsuarioVer.as_view(), name='ver'),
	path('editar/<int:pk>', views.UsuarioEditar.as_view(), name='editar'),
	path('eliminar/<int:pk>', views.UsuarioEliminar.as_view(), name='eliminar'),
]

# Copyright: Null Pointers 2021