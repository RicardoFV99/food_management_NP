from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
	path('', views.landing_page, name='landing_page'),
	path('home/', views.home, name='home'),
	path('login/', views.Login.as_view(), name='log_in'),
	path('signin/', views.SignupOrganizacion.as_view(), name='sign_in'),
	path('change-password/', views.UpdatePassword.as_view(), name="update_password"),
	path('logout/', LogoutView.as_view(), name='logout'),
]

# Copyright: Null Pointers 2021