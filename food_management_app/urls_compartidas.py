from django.urls import path
from . import views

app_name = 'compartidas'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignupOrganizacion.as_view(), name='signup'),
]