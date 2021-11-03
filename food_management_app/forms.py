from django import forms
from django.forms import widgets
from .models import Usuario, Publicacion, Organizacion
#Aqui van los formularios
class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = ('first_name', 'last_name', 'email', 'cp')
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre', 'onFocus':'validar(this)'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellido', 'onFocus':'validar(this)'}),
			'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo Electrónico', 'onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código postal', 'onFocus':'validar(this)'}),
		}

class OrganizacionForm(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('first_name', 'email', 'cp','direccion','pagina_web')
		widgets = {
			'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','onFocus':'validar(this)'}),
			'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo Electrónico', 'onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Postal','onFocus':'validar(this)'}),
			'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección','onFocus':'validar(this)'}),
			'pagina_web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sitio Web'}),

		}

class OrganizacionFormSignup(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('email', 'password', 'cp', 'direccion', 'telefono', 'password')
		widgets = {
			'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo Electrónico','onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código postal','onFocus':'validar(this)'}),
			'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección','onFocus':'validar(this)'}),
			'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono','onFocus':'validar(this)'}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
		}

	def save(self, commit=True):
		user = super(OrganizacionFormSignup, self).save(commit=False)
		user.set_password(self.cleaned_data['password']) #Encripta la contraseña
		if commit:
			user.save()
		return user

class PublicacionForm(forms.ModelForm):

	class Meta:
		model = Publicacion

		fields = ('usuario', 'contenido', )
		widgets = {
			'usuario': forms.Select(attrs={'hidden': True}),
			'contenido': forms.TextInput(attrs={'placeholder': 'Escribe algo...'})
		}

class OrganizacionContra(forms.ModelForm):
    
	class Meta:
		model = Organizacion

		fields = ('password',)
		widgets = {
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
		}

	def save(self, commit=True):
		user = super(OrganizacionContra, self).save(commit=False)
		user.set_password(self.cleaned_data['password']) #Encripta la contraseña
		if commit:
			user.save()
		return user

# Copyright: Null Pointers 2021