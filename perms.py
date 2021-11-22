import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_management.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from food_management_app.models import Usuario, Organizacion

grupo_organizaciones = Group.objects.create(name='organizaciones')
grupo_usuarios = Group.objects.create(name='usuarios')

content_type = ContentType.objects.get_for_model(Usuario)
permiso_usuarios = Permission.objects.create(
    codename = 'permiso_usuarios',
    name = 'Permiso requerido para el grupo usuarios',
    content_type = content_type
)

content_type2 = ContentType.objects.get_for_model(Organizacion)
permiso_organizaciones = Permission.objects.create(
    codename = 'permiso_organizaciones',
    name = 'Permiso requerido para el grupo de organizaciones',
    content_type = content_type2
)

grupo_usuarios.permissions.add(permiso_usuarios)
grupo_organizaciones.permissions.add(permiso_organizaciones)

organizacion = Organizacion.objects.create_user(first_name='Comex_org', username="comex_org@comex.com", email= 'comex_org@comex.com', password='comex', direccion="Comex", cp=98080, telefono=1231234123)
organizacion.groups.add(grupo_organizaciones)
usuario = Usuario.objects.create_user(first_name='Comex_user', username="comex_usr@comex.com", email='comex_usr@gmail.com', password='comex', cp=99990)
usuario.groups.add(grupo_usuarios)
Usuario.objects.create_superuser(first_name='admin', username="admin", email="admin@admin.com", password='admin', cp=99990)