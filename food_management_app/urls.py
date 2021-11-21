from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
	path('', views.landing_page, name='landing_page'),
	path('home/', views.home, name='home'),
	path('signin/', views.signin, name='signin'),
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('change-password/', views.UpdatePassword.as_view(), name="update_password"),
]

# Copyright: Null Pointers 2021