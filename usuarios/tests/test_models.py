# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: test_models.py
#
# Descripción:
#    El archivo contiene las pruebas para
#    probar el correcto funcionamiento de
#    los modelos de la aplicación usuarios.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django.core.exceptions import ValidationError
from django.test import TestCase

from usuarios.models import Donador, Organizacion


class TestModels(TestCase):


	# Donador


	def test_retrieve_donador(self):
		nuevo_donador = self.crear_donador()
		nuevo_donador.full_clean()
		nuevo_donador.save()
		self.assertEqual(
			Donador.objects.first().username,
			nuevo_donador.__str__())

	def test_agrega_donador(self):
		nuevo_donador = self.crear_donador()

		primer_donador = Donador.objects.first()

		self.assertEqual(primer_donador, nuevo_donador)
		self.assertEqual(primer_donador.first_name, 'Scott')
		self.assertEqual(str(primer_donador), 'scottwozniak@scottthewoz.com')
		self.assertEqual(len(Donador.objects.all()), 1)
	
	def test_donador_codigo_postal_no_valido(self):
		nuevo_postulante = Donador.objects.create(
			first_name = 'Scott',
			username = 'scottwozniak@scottthewoz.com',
			email = 'scottwozniak@scottthewoz.com',
			password = 'scatt',
			codigo_postal = 123456
		)

		with self.assertRaises(ValidationError):
			nuevo_postulante.full_clean()

	def crear_donador(self):
		return Donador.objects.create(
			first_name = 'Scott',
			username = 'scottwozniak@scottthewoz.com',
			email = 'scottwozniak@scottthewoz.com',
			password = 'scatt',
			codigo_postal = 12345
		)


	# Organizacion


	def test_retrieve_organizacion(self):
		nueva_organizacion = self.crear_organizacion()
		nueva_organizacion.full_clean()
		nueva_organizacion.save()
		self.assertEqual(
			Organizacion.objects.first().username,
			nueva_organizacion.__str__())

	def test_agrega_organizacion(self):
		nueva_organizacion = self.crear_organizacion()

		primer_organizacion = Organizacion.objects.first()

		self.assertEqual(primer_organizacion, nueva_organizacion)
		self.assertEqual(primer_organizacion.first_name, 'Scott')
		self.assertEqual(str(primer_organizacion), 'scottwozniak@scottthewoz.com')
		self.assertEqual(len(Donador.objects.all()), 1)
	
	def test_organizacion_codigo_postal_no_valido(self):
		nuevo_postulante = Organizacion.objects.create(
			first_name = 'Scott',
			username = 'scottwozniak@scottthewoz.com',
			email = 'scottwozniak@scottthewoz.com',
			password = 'scatt',
			direccion = 'Ohayo',
			telefono = 1999999999,
			codigo_postal = 123451
		)

		with self.assertRaises(ValidationError):
			nuevo_postulante.full_clean()
	
	def crear_organizacion(self):
		return Organizacion.objects.create(
			first_name = 'Scott',
			username = 'scottwozniak@scottthewoz.com',
			email = 'scottwozniak@scottthewoz.com',
			password = 'scatt',
			direccion = 'Ohayo',
			telefono = 1999999999,
			codigo_postal = 12345
		)

# Copyright: Null Pointers 2021