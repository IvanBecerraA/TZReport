from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Q

from django.views.generic import ListView, View
from tzapp.utils import pdfConvert
from tzapp.models import *
from .import forms




class ListaRepo001(ListView):
    model = DetalleCamionRecepcionLeche
    template_name = "reporte/repo001.html"
    context_object_name = 'repos001'

class ListaRepo001Pdf(View):
    
    def get(self, request, *args, **kwargs):
        repos001 = DetalleCamionRecepcionLeche.objects.all()
        data = {
            'repos001': repos001
        }
        pdf = pdfConvert('reporte/repo001pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Create your views here.
@login_required #decorador para asegurarnos de que sólo se permita el acceso a esta vista a usuarios autenticados.
def menuReporte(request):
    return render(request, 'reporte/menureportes.html')

@login_required
def index(request):
    return render(request,'index\index.html')

def salir(request):
    logout(request)
    return redirect('/')

#-------------------------------------- Inicio de los views para la RE PO 001 --------------------------------------

#Esta es una función de vista en Django que muestra una lista de objetos "DetalleCamionRecepcionLeche" ordenados por fecha en orden descendente.
@login_required
def repo001Listar(request):
    repos001 = DetalleCamionRecepcionLeche.objects.order_by('-fecha')
    # La función utiliza un objeto "Paginator" de Django para dividir la lista de objetos en páginas de tamaño "5", y luego obtiene la página actual a partir de la solicitud GET y obtiene los objetos de esa página.
    paginator = Paginator(repos001, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)
    data = {'repos001': objetos_pagina, 'page':page}
    #data={'repos001': repos001}
    # Finalmente, la función renderiza una plantilla HTML llamada "listar.html" y le pasa los objetos de la página actual como el contexto.
    return render(request, 'repo001/listar.html', data)

@login_required
def repo001Buscar(request):
    repos001 = DetalleCamionRecepcionLeche.objects.order_by('-fecha')
    if request.method == "GET":
        query = request.GET.get('repo001_buscar')
        queryset = repos001.filter(Q(fecha__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos001 = paginator.page(page)
        #queryset = repos001.filter(Q(fecha__icontains = query) | Q(tcl__icontains = query))
        total = queryset.count()
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos001':repos001,
        }
        return render(request, 'repo001/buscar.html', data)

@login_required
def repo001Agregar(request):
    form=forms.Repo001Form()
    if request.method == 'POST':
        form=forms.Repo001Form(request.POST)
        if form.is_valid():
            #registrar usuario autenticado en el formulario
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            #return repo001Listar(request)
            return redirect('/repo001_listar')
    data={'form':form}
    return render(request, 'repo001/agregar.html', data)

@login_required
def repo001Eliminar(request, id):
    registro = get_object_or_404(DetalleCamionRecepcionLeche, pk=id)
    registro.delete()
    return redirect('repo001_listar')

@login_required
def repo001Editar(request, id):
    registro = get_object_or_404(DetalleCamionRecepcionLeche, pk=id)
    
    if request.method == 'POST':
        form=forms.Repo001Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            #return repo001Listar(request)
            return redirect('/repo001_listar')
    else:
        form=forms.Repo001Form(instance=registro)
    data={'form':form}
    return render(request, 'repo001/editar.html', data)

@login_required
def operadorAgregar(request):
    nombre_modelo = Operador.__name__
    form=forms.OperadorForm()
    if request.method == 'POST':
        form=forms.OperadorForm(request.POST)
        if form.is_valid():
            form.save()
            # return repo001Agregar(request)
            return redirect('/repo001_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def placaAgregar(request):
    nombre_modelo = Camion.__name__
    form=forms.CamionForm()
    if request.method == 'POST':
        form=forms.CamionForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('/repo001_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def recorridoAgregar(request):
    nombre_modelo = Recorrido.__name__
    form=forms.RecorridoForm()
    if request.method == 'POST':
        form=forms.RecorridoForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('/repo001_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def tlcAgregar(request):
    nombre_modelo = Tlc.__name__
    form=forms.TlcForm()
    if request.method == 'POST':
        form=forms.TlcForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('/repo001_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)


#-------------------------------------- Fin de los views para la RE PO 001 --------------------------------------



#-------------------------------------- Inicio de los views para la RE PO 013 --------------------------------------

@login_required #si o si estar logeafo
def repo013Listar(request):
    repos013 = Detalle_pasteurizacion.objects.order_by('-fecha_registro')
    data={'repos013': repos013}
    return render(request, 'repo013/listar.html', data)

@login_required
def repo013Agregar(request):
    form=forms.Repo013Form()
    if request.method == 'POST':
        form=forms.Repo013Form(request.POST)
        if form.is_valid():
            form.save()
            return repo013Listar(request)
    data={'form':form}
    return render(request, 'repo013/agregar.html', data)

@login_required
def repo013Eliminar(request, id):
    registro = get_object_or_404(Detalle_pasteurizacion, pk=id)
    registro.delete()
    return redirect('repo013_listar')

@login_required
def repo013Editar(request, id):
    registro = get_object_or_404(Detalle_pasteurizacion, pk=id)
    
    if request.method == 'POST':
        form=forms.Repo013Form(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            #return repo001Listar(request)
            return redirect('/repo013_listar')
    else:
        form=forms.Repo013Form(instance=registro)
    data={'form':form}
    return render(request, 'repo013/editar.html', data)

@login_required
def tctAgregar(request):
    nombre_modelo = Tct.__name__
    form=forms.TctForm()
    if request.method == 'POST':
        form=forms.TctForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('/repo013_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def tlpAgregar(request):
    nombre_modelo = Tlp.__name__
    form=forms.TlpForm()
    if request.method == 'POST':
        form=forms.TlpForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('/repo013_agregar')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

#-------------------------------------- Fin de los views para la RE PO 013 --------------------------------------
