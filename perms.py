# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: perms.py
#
# Descripción:
#    El archivo contiene un script para crear los
#    grupos y permisos de la aplicación, además
#    de crear un super usuario para administrar los
#    datos.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_management.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from usuarios.models import Organizacion

# Se crea el grupo para las organizaciones.
organizaciones = Group.objects.create(name='Organizaciones')

# Se crea el permiso para crear publicaciones.
crear_publicaciones = Permission.objects.create(
	codename = 'crear_publicaciones',
	name = 'Crear Publicaciones',
	content_type = ContentType.objects.get_for_model(Organizacion)
)

# Se crea el permiso para editar publicaciones.
editar_publicaciones = Permission.objects.create(
	codename = 'editar_publicaciones',
	name = 'Editar Publicaciones',
	content_type = ContentType.objects.get_for_model(Organizacion)
)

# Se crea el permiso para eliminar publicaciones.
eliminar_publicaciones = Permission.objects.create(
	codename = 'eliminar_publicaciones',
	name = 'Eliminar Publicaciones',
	content_type = ContentType.objects.get_for_model(Organizacion)
)

#Se agregan los permisos al grupo de organizaciones.
organizaciones.permissions.add(crear_publicaciones)
organizaciones.permissions.add(editar_publicaciones)
organizaciones.permissions.add(eliminar_publicaciones)

# Se crea una organización por defecto.
organizacion = Organizacion.objects.create(
	first_name = 'Comex',
	username = 'ventas@comex.com',
	email =  'ventas@comex.com',
	password = 'ventas_comex',
	direccion = 'Avenida Heroico Colegio Militar 74, Guadalupe Centro',
	codigo_postal = 98600,
	telefono = 4928995961
)

# Se le asigna el grupo a la organizacion recién creada.
organizacion.groups.add(organizaciones)

# Se crea un superuser por cada integrante del equipo en la aplicación.
# Isaac Alejandro Díaz López
User.objects.create_superuser(username='34154287', email='34154287@uaz.edu.mx', password='34154287')
# Ricardo Flores Vázquez
User.objects.create_superuser(username='35166006', email='35166006@uaz.edu.mx', password='35166006')
# Erick Alexandro Pinales González
User.objects.create_superuser(username='38192828', email='38192828@uaz.edu.mx', password='38192828')
# Kevin Javier Reyes Medina
User.objects.create_superuser(username='38192831', email='38192831@uaz.edu.mx', password='38192831')

# Copyright: Null Pointers 2021