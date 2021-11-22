from django.urls import path

from . import views

app_name = 'organizacion'

urlpatterns = [
	path('mi-perfil/', views.OrganizacionVer.as_view(), name='ver'),
	path('editar-perfil/', views.OrganizacionEditar.as_view(), name='editar'),
	path('eliminar-cuenta/', views.OrganizacionEliminar.as_view(), name='eliminar'),
    #path('pdf-datos-org/<int:pk>', views.DatosOrganizacionPDF.as_view(), name='pdf_datos_org'),
    path('pdf-datos-org/<int:pk>', views.PdfDetallesOrganizacion.as_view(), name='pdf_datos_org'),

]

# Copyright: Null Pointers 2021