from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_weasyprint import WeasyTemplateResponseMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
from django.contrib.auth.models import Group 


from .models import Usuario, Organizacion, Publicacion
from .forms import UsuarioCreateForm, UsuarioUpdateForm, OrganizacionCreateForm, OrganizacionUpdateForm, PublicacionCreateForm, PublicacionUpdateForm


def landing_page(request):
	return render(request, 'landing_page.html', {})

def home(LoginRequiredMixin, request):
	publicaciones = Publicacion.objects.order_by('-fecha_hora')

	return render(request, 'home.html', {'publicaciones': publicaciones})

def error_404(request, exception):
    return render(request, '404.html', {})


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
			return redirect('login')

	return render(request, 'signin.html', {})

class UpdatePassword(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = 'food_management_app/change-password.html'
	success_url = reverse_lazy('home')


#############################
#          USUARIO          #
#############################


class UsuarioVer(LoginRequiredMixin, DetailView):
	model = Usuario

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Usuario.objects.get(username=pk)
		return obj

class UsuarioEditar(LoginRequiredMixin, UpdateView):
	model = Usuario
	form_class = UsuarioUpdateForm
	success_url = reverse_lazy('usuario:ver')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Usuario.objects.get(username=pk)
		return obj

class UsuarioEliminar(LoginRequiredMixin, DeleteView):
	model = Usuario
	success_url = reverse_lazy('landing_page')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Usuario.objects.get(username=pk)
		return obj


#############################
#        ORGANIZACIÓN       #
#############################


class OrganizacionVer(LoginRequiredMixin, DetailView):
	model = Organizacion

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Organizacion.objects.get(username=pk)
		return obj

class OrganizacionEditar(LoginRequiredMixin, UpdateView):
	model = Organizacion
	form_class = OrganizacionUpdateForm
	success_url = reverse_lazy('organizacion:ver')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Organizacion.objects.get(username=pk)
		return obj

class OrganizacionEliminar(LoginRequiredMixin, DeleteView):
	model = Organizacion
	success_url = reverse_lazy('logout')

	def get_object(self, queryset=None):
		pk = self.request.user.username
		obj = Organizacion.objects.get(username=pk)
		return obj
     
class DatosOrganizacionPDF(DetailView):
    model = Organizacion
    template_name = 'food_management_app/organizacion_pdf.html'

class PdfDetallesOrganizacion(WeasyTemplateResponseMixin, DatosOrganizacionPDF):
    pdf_attachment = False
    pdf_filename = 'food_management_app/organizacion_detail.html.pdf'


#############################
#        PUBLICACION        #
#############################


# perms.food_management_app.permiso_organizaciones
class PublicacionNueva(PermissionRequiredMixin, CreateView):
	permission_required = 'food_management_app.permiso_organizaciones'
	model = Publicacion
	form_class = PublicacionCreateForm
	success_url = reverse_lazy('home')

	extra_context = {
		'etiqueta': 'Crear',
		'boton': 'Publicar'
	}

	def form_valid(self, form):
		usuario = get_object_or_404(Organizacion, id=self.request.user.id)
		form.instance.usuario = usuario
		return super().form_valid(form)

# perms.food_management_app.permiso_organizaciones
class PublicacionEditar(PermissionRequiredMixin, UpdateView):
	permission_required = 'food_management_app.permiso_organizaciones'
	model = Publicacion
	form_class = PublicacionUpdateForm
	success_url = reverse_lazy('home')

	extra_context = {
		'etiqueta': 'Editar',
		'boton': 'Guardar Cambios'
	}

# perms.food_management_app.permiso_organizaciones
class PublicacionEliminar(PermissionRequiredMixin, DeleteView):
	permission_required = 'food_management_app.permiso_organizaciones'
	model = Publicacion
	success_url = reverse_lazy('home')

# Copyright: Null Pointers 2021