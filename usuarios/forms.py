# -*- coding: UTF-8 -*-
#-----------------------------------------------------
# Archivo: forms.py
#
# Descripción:
#    El archivo contiene las declaraciones de los
#    formularios de la aplicación de usuarios para así
#    utilizarlos en las vistas que los requieran.
#
# Equipo:
#    - Isaac Alejandro Díaz López
#    - Ricardo Flores Vázquez
#    - Erick Alexandro Pinalez Gonzáles
#    - Kevin Javier Reyes Medina
#
#-----------------------------------------------------

from django import forms
from django.contrib.auth.models import Group

from .models import Donador, Organizacion


class DonadorCreateForm(forms.ModelForm):
	class Meta:
		model = Donador

		fields = ('first_name', 'email', 'password', 'codigo_postal')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
			'codigo_postal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'}),
		}

		labels = {
			'first_name': 'Nombre',
			'email': 'Correo Electrónico',
			'password': 'Contraseña',
			'codigo_postal': 'Código Postal'
		}
	
	def save(self, commit=True):
		user = super(DonadorCreateForm, self).save(commit=False)
		user.username = user.email
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()
		
		return user


class DonadorUpdateForm(forms.ModelForm):
	class Meta:
		model = Donador

		fields = ('first_name', 'last_name', 'email', 'codigo_postal')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Nombre'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Apellidos'}),
			'email': forms.EmailInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Correo Electrónico'}),
			'codigo_postal': forms.NumberInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Código Postal'}),
		}

		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'email': 'Correo Electrónico',
			'codigo_postal': 'Código Postal'
		}
	
	def save(self, commit=True):
		user = super(DonadorUpdateForm, self).save(commit=False)
		user.username = user.email

		if commit:
			user.save()
		
		return user


class OrganizacionCreateForm(forms.ModelForm):
	class Meta:
		model = Organizacion

		fields = ('first_name', 'email', 'password', 'direccion', 'telefono', 'codigo_postal')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
			'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
			'codigo_postal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Código Postal'}),
		}

		labels = {
			'first_name': 'Nombre',
			'email': 'Correo Electrónico',
			'password': 'Contraseña',
			'direccion': 'Dirección',
			'telefono': 'Teléfono',
			'codigo_postal': 'Código Postal'
		}

	def save(self, commit=True):
		user = super(OrganizacionCreateForm, self).save(commit=False)
		user.username = user.email
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()
			user.groups.add(Group.objects.get(id=1))
		
		return user


class OrganizacionUpdateForm(forms.ModelForm):
	class Meta:
		model = Organizacion

		fields = ('first_name', 'email', 'pagina_web', 'direccion', 'telefono', 'codigo_postal')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Nombre'}),
			'email': forms.EmailInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Correo Electrónico'}),
			'pagina_web': forms.TextInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Página Web'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Dirección'}),
			'telefono': forms.NumberInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Teléfono'}),
			'codigo_postal': forms.NumberInput(attrs={'class': 'form-control form-control-edit', 'placeholder': 'Código Postal'}),
		}

		labels = {
			'first_name': 'Nombre',
			'email': 'Correo Electrónico',
			'pagina_web': 'Página Web',
			'direccion': 'Dirección',
			'telefono': 'Teléfono',
			'codigo_postal': 'Código Postal'
		}
	
	def save(self, commit=True):
		user = super(OrganizacionUpdateForm, self).save(commit=False)
		user.username = user.email

		if commit:
			user.save()
		
		return user

class CambiarContrasenaForm(forms.ModelForm):
	class Meta:
		model = Donador

		fields = ('password', )
	
	def save(self, commit=True):
		user = super(CambiarContrasenaForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()
		
		return user

# Copyright: Null Pointers 2021