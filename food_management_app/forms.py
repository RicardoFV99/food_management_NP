from django import forms
from .models import Usuario, Publicacion, Organizacion

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = ('username','cp')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código postal','onFocus':'validar(this)'}),
		}

	def save(self, commit=True):
		user = super(UsuarioForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password']) #Encripta la contraseña
		if commit:
			user.save()
		return user

class OrganizacionForm(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('username','cp','direccion','telefono','pagina_web')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código postal','onFocus':'validar(this)'}),
			'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección','onFocus':'validar(this)'}),
			'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono','onFocus':'validar(this)'}),
			'pagina_web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Página web','onFocus':'validar(this)'}),

		}
	
class OrganizacionFormSignup(forms.ModelForm):

	class Meta:
		model = Organizacion

		fields = ('username','cp','direccion','telefono','pagina_web','password')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre','onFocus':'validar(this)'}),
			'cp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código postal','onFocus':'validar(this)'}),
			'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección','onFocus':'validar(this)'}),
			'telefono':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono','onFocus':'validar(this)'}),
			'pagina_web':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Página web','onFocus':'validar(this)'}),
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

		fields = '__all__'

# Copyright: Null Pointers 2021