from django.urls import path
from . import views

app_name = 'organizacion'

urlpatterns = [
    path('lista/', views.Lista_organizaciones.as_view(), name='lista'),
    path('eliminar/<int:pk>', views.Eliminar_organizacion.as_view(), name='eliminar'),
    path('editar/<int:pk>', views.Editar_organizacion.as_view(), name='editar'),
    path('nuevo/', views.Nueva_organizacion.as_view(), name='nuevo'),
    path('editar-perfil/<int:pk>', views.EditarPerfil.as_view(), name='editar-perfil'),
    path('ver/<int:pk>', views.OrganizacionDetalle.as_view(), name='ver'),
]