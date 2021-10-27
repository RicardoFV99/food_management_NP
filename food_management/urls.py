from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('food_management_app.urls')),
	path('usuario/', include('food_management_app.urls_usuario')),
	path('organizacion/', include('food_management_app.urls_organizacion')),
	path('publicacion/', include('food_management_app.urls_publicacion')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Copyright: Null Pointers 2021