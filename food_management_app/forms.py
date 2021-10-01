from django import forms
from .models import Usuario, Publicacion, Organizacion


class OrganizacionForm(forms.ModelForm):

    class Meta:
        model = Organizacion

        fields = '__all__'

class PublicacionForm(forms.ModelForm):
    
    class Meta:
        model = Publicacion

        fields = '__all__'