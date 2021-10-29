from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Usuario(User):
	cp = models.CharField(max_length = 5)

	def __str__(self):
		return self.username 

class Organizacion(Usuario):
	direccion = models.CharField(max_length = 150)
	telefono = models.CharField(max_length = 150)
	pagina_web = models.CharField(max_length = 150)
	visibilidad=models.BooleanField(default=1)
	def __str__(self):
		return self.username

class Publicacion(models.Model):
	usuario = models.ForeignKey("food_management_app.Organizacion", verbose_name="Organizacion", on_delete=models.CASCADE)
	contenido = models.CharField(max_length = 300)
	fecha_hora = models.DateTimeField(default=now, editable=False)

# Copyright: Null Pointers 2021