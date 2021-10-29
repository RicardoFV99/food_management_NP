from django.urls import path

from . import views

app_name = 'publicacion'

urlpatterns = [
	path('nuevo/', views.PublicacionNueva.as_view(), name='nuevo'),
	path('editar/<int:pk>', views.PublicacionEditar.as_view(), name='editar'),
	path('eliminar/<int:pk>', views.PublicacionEliminar.as_view(), name='eliminar'),
]

# Copyright: Null Pointers 2021