"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from tzapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('salir/', salir, name='salir'),
    path('repo001_listar/', repo001Listar, name='repo001_listar'),
    path('repo001_agregar/', repo001Agregar, name='repo001_agregar'),
    path('repo001_eliminar/<int:id>', repo001Eliminar, name='repo001_eliminar'),
    path('operador_agregar/', operadorAgregar, name='operador_agregar'),
    path('placa_agregar/', placaAgregar, name='placa_agregar'),
    path('recorrido_agregar/', recorridoAgregar, name='recorrido_agregar'),
    path('tlc_agregar/', tlcAgregar, name='tlc_agregar'),
    
]
