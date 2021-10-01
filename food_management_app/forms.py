from django import forms
from .models import Usuario, Publicacion, Organizacion


class OrganizacionForm(forms.ModelForm):

    class Meta:
        model = Organizacion

        fields = '__all__'