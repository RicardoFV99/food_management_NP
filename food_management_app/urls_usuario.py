from django.urls import path

from . import views

app_name = 'usuario'

urlpatterns = [
	path('mi-perfil/', views.UsuarioVer.as_view(), name='ver'),
	path('editar-perfil/', views.UsuarioEditar.as_view(), name='editar'),
	path('eliminar-cuenta/', views.UsuarioEliminar.as_view(), name='eliminar'),
]

# Copyright: Null Pointers 2021