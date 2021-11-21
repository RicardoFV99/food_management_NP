from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.backends import ModelBackend
from django.utils.timezone import now

User._meta.get_field('first_name').null = False # The email field is modified to avoid being null on DB.
User._meta.get_field('first_name').blank = False # The email field is modified to avoid being blank on front-end

User._meta.get_field('email')._unique = True # The email field is modified to be unique.
User._meta.get_field('email').null = False # The email field is modified to avoid being null on DB.
User._meta.get_field('email').blank = False # The email field is modified to avoid being blank on front-end


class Usuario(User):
	cp = models.IntegerField('Código Postal', validators=[MinValueValidator(00000), MaxValueValidator(99999)])

	def __str__(self):
		return self.username 

class Organizacion(Usuario):
	direccion = models.CharField('Dirección', max_length = 50)
	telefono = models.IntegerField('Teléfono', validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)])
	pagina_web = models.CharField(max_length = 25, blank=True, null=True)
	visibilidad = models.BooleanField(default=True)

class Publicacion(models.Model):
	usuario = models.ForeignKey("food_management_app.Organizacion", verbose_name="Organizacion", blank=True, null=True, on_delete=models.CASCADE)
	contenido = models.CharField(max_length = 300)
	fecha_hora = models.DateTimeField(default=now, editable=False)

#class EmailBackend(ModelBackend):
#	def authenticate(self, request, username=None, password=None, **kwargs):
#		UserModel = get_user_model()
#		try:
#			user = UserModel.objects.get(email=username)
#		except UserModel.DoesNotExist:
#			return None
#		else:
#			if user.check_password(password):
#				return user
#		return None

# Copyright: Null Pointers 2021