from django.urls import path
from . import views

app_name = 'publicacion'

urlpatterns = [
    path('lista/', views.Lista_publicaciones.as_view(), name='lista'),
    path('eliminar/<int:pk>', views.Eliminar_publicacion.as_view(), name='eliminar'),
    path('editar/<int:pk>', views.Editar_publicacion.as_view(), name='editar'),
    path('nuevo/', views.Nueva_publicacion.as_view(), name='nuevo'),
]