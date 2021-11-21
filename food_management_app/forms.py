from django import forms
from django.forms import widgets

from .models import Usuario, Publicacion, Organizacion


class UsuarioCreateForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = ('first_name', 'last_name', 'email', 'password', 'cp')

		widgets = {
			'firts_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'cp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
		}

		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo Electrónico',
			'password': 'Contraseña',
			'cp': 'Código Postal',
		}

	def save(self, commit=True):
		user = super(UsuarioCreateForm, self).save(commit=False)
		user.username = user.email
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()

		return user


class UsuarioUpdateForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = ('first_name', 'last_name', 'email', 'cp')

		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'cp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
		}

		labels = {
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo Electrónico',
			'cp': 'Código Postal',
		}


class OrganizacionCreateForm(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('first_name', 'email', 'password', 'direccion', 'cp' , 'telefono', 'pagina_web')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'cp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'pagina_web': forms.TextInput(attrs={'class': 'form-control'}),
		}

		labels = {
			'first_name': 'Nombre',
			'email': 'Correo Electrónico',
			'password': 'Contraseña',
			'direccion': 'Dirección',
			'cp': 'Código Postal',
			'telefono': 'Teléfono',
			'pagina_web': 'Página Web',
		}

	def save(self, commit=True):
		user = super(OrganizacionCreateForm, self).save(commit=False)
		user.username = user.email
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()

		return user

class OrganizacionUpdateForm(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('first_name', 'email', 'direccion', 'cp' , 'telefono', 'pagina_web')

		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'cp': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Obligatorio'}),
			'pagina_web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Página Web'}),
		}

		labels = {
			'first_name': 'Nombre',
			'email': 'Correo Electrónico',
			'direccion': 'Dirección',
			'cp': 'Código Postal',
			'telefono': 'Teléfono',
			'pagina_web': 'Página Web',
		}


class PublicacionCreateForm(forms.ModelForm):

	class Meta:
		model = Publicacion

		fields = ('usuario', 'contenido')

		widgets = {
			'usuario': forms.Select(attrs={'hidden': True}),
			'contenido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación...'})
		}

class PublicacionUpdateForm(forms.ModelForm):

	class Meta:
		model = Publicacion

		fields = ('contenido', )

		widgets = {
			'contenido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contenido de la publicación...'})
		}

#class OrganizacionContra(forms.ModelForm):
#		
#	class Meta:
#		model = Organizacion
#
#		fields = ('password',)
#		widgets = {
#			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
#		}
#
#	def save(self, commit=True):
#		user = super(OrganizacionContra, self).save(commit=False)
#		user.set_password(self.cleaned_data['password']) #Encripta la contraseña
#		if commit:
#			user.save()
#		return user

# Copyright: Null Pointers 2021