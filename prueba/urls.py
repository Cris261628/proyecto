"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from django.conf.urls.static import static 
from registros import views as views_registros
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros,name="principal"),
    path('contacto/',views_registros.contacto,name="contacto"),
    path('formulario/',views.formulario,name="formulario"),
    path('ejemplo/',views.ejemplo,name="ejemplo"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('comentarios/',views_registros.comentarios,name="comentarios"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('consultas1',views_registros.consultar,name="consultas"),

    path('consultasSQL',views_registros.consultasSQL,name="sql"),
    path('seguridad',views_registros.seguridad,name="Seguridad"),
]   
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    