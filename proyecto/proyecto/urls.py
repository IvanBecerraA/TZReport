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
    path('menu_reporte/', menuReporte ,name='menureporte'),
    path('reporte/', ListaRepo001.as_view(), name='reporte'),
    path('reportepdf/', ListaRepo001Pdf.as_view(), name='reportepdf'),
    #-------------------------------------- Inicio de las urls para la RE PO 001 --------------------------------------
    path('repo001_listar/', repo001Listar, name='repo001_listar'),
    path('repo001_buscar/', repo001Buscar, name='repo001_buscar'),
    path('repo001_agregar/', repo001Agregar, name='repo001_agregar'),
    path('repo001_eliminar/<int:id>', repo001Eliminar, name='repo001_eliminar'),
    path('repo001_editar/<int:id>', repo001Editar, name='repo001_editar'),
    path('operador_agregar/', operadorAgregar, name='operador_agregar'),
    path('placa_agregar/', placaAgregar, name='placa_agregar'),
    path('recorrido_agregar/', recorridoAgregar, name='recorrido_agregar'),
    path('tlc_agregar/', tlcAgregar, name='tlc_agregar'),
    #-------------------------------------- Termino de las urls para la RE PO 001 --------------------------------------
    #-------------------------------------- Inicio de las urls para la RE PO 013 --------------------------------------
    path('repo013_listar/', repo013Listar, name='repo013_listar'),
    path('repo013_buscar/', repo013Buscar, name='repo013_buscar'),
    path('repo013_agregar/', repo013Agregar, name='repo013_agregar'),
    path('repo013_eliminar/<int:id>', repo013Eliminar, name='repo013_eliminar'),
    path('repo013_editar/<int:id>', repo013Editar, name='repo013_editar'),
    path('tct_agregar/', tctAgregar, name='tct_agregar'),
    path('tlp_agregar/', tlpAgregar, name='tlp_agregar'),
    #-------------------------------------- Termino de las urls para la RE PO 013 --------------------------------------
    #-------------------------------------- Inicio de las urls para la RE PO 003 --------------------------------------
    path('repo003_listar/', repo003Listar, name='repo003_listar'),
    path('repo003_buscar/', repo003Buscar, name='repo003_buscar'),
    path('repo003_agregar/', repo003Agregar, name='repo003_agregar'),
    path('repo003_eliminar/<int:id>', repo003Eliminar, name='repo003_eliminar'),
    path('repo003_editar/<int:id>', repo003Editar, name='repo003_editar'),
    path('tmy_agregar/', tmyAgregar, name='tmy_agregar'),
    path('maquina_agregar/', maquinaAgregar, name='maquina_agregar'),
    #-------------------------------------- Termino de las urls para la RE PO 003 --------------------------------------
    #-------------------------------------- Inicio de las urls para la RE PO 004 --------------------------------------
    path('repo004_listar/', repo004Listar, name='repo004_listar'),
    path('repo004_buscar/', repo004Buscar, name='repo004_buscar'),
    path('repo004_agregar/', repo004Agregar, name='repo004_agregar'),
    path('repo004_eliminar/<int:id>', repo004Eliminar, name='repo004_eliminar'),
    path('repo004_editar/<int:id>', repo004Editar, name='repo004_editar'),
    
    

]
