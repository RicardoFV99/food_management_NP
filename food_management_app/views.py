from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_weasyprint import WeasyTemplateResponseMixin


from .models import Usuario, Organizacion, Publicacion
from .forms import UsuarioCreateForm, UsuarioUpdateForm, OrganizacionCreateForm, OrganizacionUpdateForm, PublicacionCreateForm, PublicacionUpdateForm


def landing_page(request):
	return render(request, 'landing_page.html', {})

def home(request):
	publicaciones = Publicacion.objects.all()

	return render(request, 'home.html', {'publicaciones': publicaciones})


#############################
#           LOGIN           #
#############################


class Login(LoginView):
	model = Usuario
	template_name = 'login.html'

def signin(request):
	if request.POST:
		if request.POST.get("es_organizacion", None):
			form = OrganizacionCreateForm(request.POST)
		else:
			form = UsuarioCreateForm(request.POST)

		if form.is_valid():
			form.save()
			return render(request, 'login.html', {})

	return render(request, 'signin.html', {})

class UpdatePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('logout')
	template_name = 'food_management_app/change-password.html'


#############################
#          USUARIO          #
#############################


class UsuarioVer(DetailView):
	model = Usuario

class UsuarioEditar(UpdateView):
	model = Usuario
	form_class = UsuarioUpdateForm
	success_url = reverse_lazy('home')

class UsuarioEliminar(DeleteView):
	model = Usuario
	success_url = reverse_lazy('landing_page')


#############################
#        ORGANIZACIÓN       #
#############################


class OrganizacionVer(DetailView):
	model = Organizacion

class OrganizacionEditar(UpdateView):
	model = Organizacion
	form_class = OrganizacionUpdateForm
	success_url = reverse_lazy('home')

class OrganizacionEliminar(DeleteView):
	model = Organizacion
	success_url = reverse_lazy('logout')
     
class DatosOrganizacionPDF(DetailView):
    model = Organizacion
    template_name = 'food_management_app/organizacion_pdf.html'

class PdfDetallesOrganizacion(WeasyTemplateResponseMixin, DatosOrganizacionPDF):
    pdf_attachment = False
    pdf_filename = 'food_management_app/organizacion_detail.html.pdf'

#############################
#        PUBLICACION        #
#############################


class PublicacionNueva(CreateView):
	model = Publicacion
	form_class = PublicacionCreateForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		usuario = get_object_or_404(Organizacion, id=self.request.user.id)
		form.instance.usuario = usuario
		return super().form_valid(form)

class PublicacionEditar(UpdateView):
	model = Publicacion
	form_class = PublicacionUpdateForm
	success_url = reverse_lazy('home')

class PublicacionEliminar(DeleteView):
	model = Publicacion
	success_url = reverse_lazy('home')

# Copyright: Null Pointers 2021