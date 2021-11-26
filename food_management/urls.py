# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#    El archivo contiene las direcciones globales del
#    proyecto para que se pueda navegar de manera
#    correcta en el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .settings import DEBUG

urlpatterns = [
    path('', include('home.urls')),
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls'))
]

if DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))

# Copyright: Null Pointers 2021