# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#    El archivo contiene las direcciones de la
#    aplicación de usuarios para que se pueda
#    navegar de manera correcta en el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.urls import path
from django.urls.conf import include

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('mi-perfil', views.DonadorPerfil.as_view(), name='donador-mi-perfil'),
    path('editar-perfil', views.DonadorEditarPerfil.as_view(), name='donador-editar-perfil'),
    path('eliminar-cuenta', views.DonadorEliminar.as_view(), name='donador-eliminar-cuenta'),
    path('organizacion/<int:pk>', views.OrganizacionVer.as_view(), name='organizacion-ver'),
    path('organizacion/mi-perfil', views.OrganizacionPerfil.as_view(), name='organizacion-mi-perfil'),
    path('organizacion/editar-perfil', views.OrganizacionEditarPerfil.as_view(), name='organizacion-editar-perfil'),
    path('organizacion/eliminar-cuenta', views.OrganizacionEliminar.as_view(), name='organizacion-eliminar-cuenta'),
    path('cambiar-contrasena', views.CambiarContrasena.as_view(), name='cambiar-contrasena')
]

# Copyright: Null Pointers 2021