from django.urls import path

from . import views

urlpatterns = [
	path('', views.landing_page, name='landing_page'),
	path('home/', views.home, name='home'),
	path('login/', views.Login.as_view(), name='log_in'),
	path('signin/', views.SignupOrganizacion.as_view(), name='sign_in'),
]

# Copyright: Null Pointers 2021