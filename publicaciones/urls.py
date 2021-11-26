# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#    El archivo contiene las direcciones de la
#    aplicación de publicaciones para que se pueda
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

from . import views

app_name = 'publicaciones'

urlpatterns = [
    path('publicar', views.PublicacionCrear.as_view(), name='publicar'),
    path('mis-publicaciones', views.mis_publicaciones, name='mis-publicaciones'),
    path('detalles/<int:pk>', views.PublicacionVer.as_view(), name='detalles'),
    path('editar/<int:pk>', views.publicacion_editar, name='editar'),
    path('eliminar/<int:pk>', views.publicacion_eliminar, name='eliminar'),
]

# Copyright: Null Pointers 2021