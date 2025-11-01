"""
URL configuration for config project.

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

#Importa el módulo de administracción que viene integrado Django
#Esto te permite usar la URL /admin/ para acceder al panel de administrador del sitio
#Superusuarios
from django.contrib import admin
#path función que difine rutas
#include sirve para conectar o incluir las rutas de otras apps dentro de enrutador
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('inicio.urls')), #Enviar la raíz del sitio a la app 'inicio'
    path('',include('paginas.urls')), #Enrutamos a la app
    path('',include('catalogo.urls')),
]
