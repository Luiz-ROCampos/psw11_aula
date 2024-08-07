from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
