# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: urls.py
#
# Descripción:
#    El archivo contiene las direcciones de la
#    aplicación de home para que se pueda
#    navegar de manera correcta en el sistema.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
	path('', views.landing_page, name='landing_page'),
    path('home', views.home, name='home'),
	path('login', views.Login.as_view(), name='login'),
	path('signin', views.signin, name='signin'),
	path('logout', LogoutView.as_view(), name='logout'),
]

# Copyright: Null Pointers 2021