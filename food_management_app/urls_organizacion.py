from django.urls import path

from . import views

app_name = 'organizacion'

urlpatterns = [
	path('ver/<int:pk>', views.OrganizacionVer.as_view(), name='ver'),
	path('editar/<int:pk>', views.OrganizacionEditar.as_view(), name='editar'),
	path('eliminar/<int:pk>', views.OrganizacionEliminar.as_view(), name='eliminar'),
]

# Copyright: Null Pointers 2021