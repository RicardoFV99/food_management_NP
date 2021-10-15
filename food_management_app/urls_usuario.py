from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('lista/', views.Lista_usuarios.as_view(), name='lista'),
    path('eliminar/<int:pk>', views.Eliminar_usuario.as_view(), name='eliminar'),
    path('editar/<int:pk>', views.Editar_usuario.as_view(), name='editar'),
    path('nuevo/', views.Nuevo_usuario.as_view(), name='nuevo'),
]