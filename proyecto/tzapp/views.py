from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from tzapp.models import *
from .import forms

# Create your views here.
@login_required
def index(request):
    return render(request,'index\index.html')

def salir(request):
    logout(request)
    return redirect('/')

#-------------------------------------- Inicio de los views para la RE PO 001 --------------------------------------

@login_required
def repo001Listar(request):
    repos001 = DetalleCamionRecepcionLeche.objects.order_by('-fecha')
    data={'repos001': repos001}
    return render(request, 'repo001/listar.html', data)

@login_required
def repo001Agregar(request):
    form=forms.Repo001Form()
    if request.method == 'POST':
        form=forms.Repo001Form(request.POST)
        if form.is_valid():
            form.save()
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
            form.save()
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
    return render(request, 'repo001/agregarabstracto.html', data)

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
    return render(request, 'repo001/agregarabstracto.html', data)

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
    return render(request, 'repo001/agregarabstracto.html', data)

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
    return render(request, 'repo001/agregarabstracto.html', data)


#-------------------------------------- Fin de los views para la RE PO 001 --------------------------------------
