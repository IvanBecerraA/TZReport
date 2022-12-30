from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import formset_factory
from django.views.generic import ListView, View
from tzapp.utils import pdfConvert
from tzapp.models import *
from tzapp.forms import *
from django.contrib.auth.models import User
from django import forms



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

@login_required
def index(request):
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all() 
    
    return render(request,'index\index.html', {'groups':groups})

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
    
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all() 
    
    data = {'repos001': objetos_pagina, 'page':page, 'groups':groups}
    #data={'repos001': repos001}
    # Finalmente, la función renderiza una plantilla HTML llamada "listar.html" y le pasa los objetos de la página actual como el contexto.
    return render(request, 'repo001/listar.html', data)

@login_required
def repo001Buscar(request):
    repos001 = DetalleCamionRecepcionLeche.objects.order_by('-fecha')
    if request.method == "GET":
        query = request.GET.get('repo001_buscar')
        queryset = repos001.filter(Q(fecha__icontains = query))
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all() 
        
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
            'groups':groups,
        }
        return render(request, 'repo001/buscar.html', data)

@login_required
def repo001Agregar(request):
    form=Repo001Form()
    if request.method == 'POST':
        form=Repo001Form(request.POST)
        if form.is_valid():
            #registrar usuario autenticado en el formulario
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            form.save_m2m()
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
        form=Repo001Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            form.save_m2m()
            return redirect('/repo001_listar')
    else:
        form=Repo001Form(instance=registro)
    data={'form':form}
    return render(request, 'repo001/editar.html', data)

@login_required
def operadorAgregar(request):
    nombre_modelo = Operador.__name__
    form=OperadorForm()
    if request.method == 'POST':
        form=OperadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@permission_required('tzapp.add_camion')
@login_required
def placaAgregar(request):
    nombre_modelo = Camion.__name__
    form=CamionForm()
    if request.method == 'POST':
        form=CamionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def recorridoAgregar(request):
    nombre_modelo = Recorrido.__name__
    form=RecorridoForm()
    if request.method == 'POST':
        form=RecorridoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def tlcAgregar(request):
    nombre_modelo = Tlc.__name__
    form=TlcForm()
    if request.method == 'POST':
        form=TlcForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)


#-------------------------------------- Termino de los views para la RE PO 001 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 013 --------------------------------------

@login_required #si o si estar logeado
def repo013Listar(request):
    repos013 = Detalle_pasteurizacion.objects.order_by('-fecha_registro')
    paginator = Paginator(repos013, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)
    
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all() 
    
    data={
        'repos013': objetos_pagina, 'page': page, 'groups':groups,}
    return render(request, 'repo013/listar.html', data)

@login_required
def repo013Buscar(request):
    repos013 = Detalle_pasteurizacion.objects.order_by('-fecha_registro')
    if request.method == "GET":
        query = request.GET.get('repo013_buscar')
        queryset = repos013.filter(Q(fecha_registro__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos013 = paginator.page(page)
        #queryset = repos013.filter(Q(fecha__icontains = query) | Q(tcl__icontains = query))
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all() 
    
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos013':repos013,
            'groups':groups,
        }
        return render(request, 'repo013/buscar.html', data)
     
@login_required
def repo013Agregar(request):
    form=Repo013Form()
    if request.method == 'POST':
        form=Repo013Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            form.save_m2m()
            return redirect('/repo013_listar')
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
        form=Repo013Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            form.save_m2m()
            #return repo001Listar(request)
            return redirect('/repo013_listar')
    else:
        form=Repo013Form(instance=registro)
    data={'form':form}
    return render(request, 'repo013/editar.html', data)

@login_required
def tctAgregar(request):
    nombre_modelo = Tct.__name__
    form=TctForm()
    if request.method == 'POST':
        form=TctForm(request.POST)
        if form.is_valid():
            form.save()
            #return repo001Agregar(request)
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def tlpAgregar(request):
    nombre_modelo = Tlp.__name__
    form=TlpForm()
    if request.method == 'POST':
        form=TlpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

#-------------------------------------- Termino de los views para la RE PO 013 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 003 --------------------------------------

@login_required
def repo003Listar(request):
    repos003 = OrdenProceso.objects.order_by('-fecha')
    paginator = Paginator(repos003, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)
    
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all() 
        
    data = {'repos003': objetos_pagina, 'page':page, 'groups':groups}
    return render(request, 'repo003/listar.html', data)


@login_required
def repo003Buscar(request):
    repos003 = OrdenProceso.objects.order_by('-fecha')
    if request.method == "GET":
        query = request.GET.get('repo003_buscar')
        queryset = repos003.filter(Q(fecha__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos003 = paginator.page(page)
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all()
    
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos003':repos003,
            'groups':groups
        }
        return render(request, 'repo003/buscar.html', data)

@login_required
def repo003Agregar(request):
    form=Repo003Form()
    if request.method == 'POST':
        form=Repo003Form(request.POST)
        if form.is_valid():
            #registrar usuario autenticado en el formulario
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            #return repo003Listar(request)
            return redirect('/repo003_listar')
    data={'form':form}
    return render(request, 'repo003/agregar.html', data)

@login_required
def repo003Eliminar(request, id):
    registro = get_object_or_404(OrdenProceso, pk=id)
    registro.delete()
    return redirect('repo003_listar')

@login_required
def repo003Editar(request, id):
    registro = get_object_or_404(OrdenProceso, pk=id)
    
    if request.method == 'POST':
        form=Repo003Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            #return repo003Listar(request)
            return redirect('/repo003_listar')
    else:
        form=Repo003Form(instance=registro)
    data={'form':form}
    return render(request, 'repo003/editar.html', data)

@login_required
def tmyAgregar(request):
    nombre_modelo = Tmy.__name__
    form=TmyForm()
    if request.method == 'POST':
        form=TmyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def maquinaAgregar(request):
    nombre_modelo = Maquina.__name__
    form=MaquinaForm()
    if request.method == 'POST':
        form=MaquinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

#-------------------------------------- Termino de los views para la RE PO 003 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 004 --------------------------------------

@login_required
def repo004Listar(request):
    repos004 = DetalleInsumosFormulacion.objects.order_by('-fecha_fabricacion')
    listaMateriaPrima = MateriaPrima.objects.all()
    
    paginator = Paginator(repos004, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)

    user = User.objects.get(username=request.user.username)
    groups = user.groups.all()
        
    data = {'repos004': objetos_pagina, 'page':page, 'listaMateriaPrima':listaMateriaPrima, 'groups':groups}
    return render(request, 'repo004/listar.html', data)


@login_required
def repo004Buscar(request):
    repos004 = DetalleInsumosFormulacion.objects.order_by('-fecha_fabricacion')
    listaMateriaPrima = MateriaPrima.objects.all()
    if request.method == "GET":
        query = request.GET.get('repo004_buscar')
        queryset = repos004.filter(Q(fecha_fabricacion__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos004 = paginator.page(page)
        #queryset = repos004.filter(Q(fecha__icontains = query) | Q(tcl__icontains = query))
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all()
        
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos004':repos004,
            'listaMateriaPrima':listaMateriaPrima,
            'groups':groups
        }
        return render(request, 'repo004/buscar.html', data)

 
@login_required
def repo004Agregar(request):
    form=Repo004Form(request.POST or None)
    
    formMateriaPrima = formset_factory(MateriaPrimaForm, extra=1)
    
    if request.method == 'POST':
        
        formMateriaPrima = formMateriaPrima(request.POST)
        
        if form.is_valid() and formMateriaPrima.is_valid():
            obj2 = form.save(commit=False)
            obj2.usuario_del_registro = request.user.username
            obj2.save()
            for f in formMateriaPrima:
                if formMateriaPrima.is_valid():
                    obj = f.save(commit=False)
                    obj.detalle_pasteurizacion_id = form.instance.id
                    obj.save()
                    
            return redirect('/repo004_listar')
        
    data={'form':form, 'formMateriaPrima':formMateriaPrima}
    return render(request, 'repo004/agregar.html', data)

@login_required
def repo004Eliminar(request, id):
    registro = get_object_or_404(DetalleInsumosFormulacion, pk=id)
    registro.delete()
    return redirect('repo004_listar')

#Editar detalle de la formulación
@login_required
def repo004Editar(request, id):
    registro = get_object_or_404(DetalleInsumosFormulacion, pk=id)
    
    if request.method == 'POST':
        form=Repo004Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            return redirect('/repo004_listar')
    else:
        form=Repo004Form(instance=registro)
        
    data={'form':form}
    return render(request, 'repo004/editar.html', data)

#Editar una materia prima del detalle de la formulación
@login_required
def repo004Editar2(request, id):
    registro = get_object_or_404(MateriaPrima, pk=id)
    
    if request.method == 'POST':
        form=MateriaPrimaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('/repo004_listar')
    else:
        form=MateriaPrimaForm(instance=registro)
        
    data={'form':form}
    return render(request, 'repo004/editar2.html', data)

#-------------------------------------- Termino de los views para la RE PO 004 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 068 --------------------------------------

@login_required
def repo068Listar(request):
    repos068 = DetalleRepo068.objects.order_by('-fecha_estandarizacion')
    paginator = Paginator(repos068, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)
    
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all()
        
    data = {'repos068': objetos_pagina, 'page':page, 'groups':groups}
    return render(request, 'repo068/listar.html', data)

@login_required
def repo068Buscar(request):
    repos068 = DetalleRepo068.objects.order_by('-fecha_estandarizacion')
    if request.method == "GET":
        query = request.GET.get('repo068_buscar')
        queryset = repos068.filter(Q(fecha_estandarizacion__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos068 = paginator.page(page)
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all()
    
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos068':repos068,
            'groups':groups
        }
        return render(request, 'repo068/buscar.html', data)

@login_required
def repo068Agregar1(request):
    productos = Producto.objects.all()
        
    data={'productos':productos}
    return render(request, 'repo068/agregar1.html', data)

@login_required
def repo068Agregar(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    
    if request.method == 'POST':
        form=Repo068Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            return redirect('/repo068_listar')
    else :
        form=Repo068Form()
        acidez_leche = form.fields['acidez_leche']
        acidez_leche.widget.attrs['min'] = acidez_leche.min_value = producto.acidez_leche_min
        acidez_leche.widget.attrs['max'] = acidez_leche.max_value = producto.acidez_leche_max
        acidez_leche.label = f'Acidez de leche: (Norma {producto.acidez_leche_min} - {producto.acidez_leche_max})'
        
        materia_grasa_leche = form.fields['materia_grasa_leche']
        materia_grasa_leche.widget.attrs['min'] = materia_grasa_leche.min_value = producto.mg_leche_min
        materia_grasa_leche.widget.attrs['max'] = materia_grasa_leche.max_value = producto.mg_leche_max
        materia_grasa_leche.label = f'Acidez de leche: (Norma {producto.mg_leche_min} - {producto.mg_leche_max})'
    
        densidad_leche = form.fields['densidad_leche']
        densidad_leche.widget.attrs['min'] = densidad_leche.min_value = producto.densidad_leche_min
        densidad_leche.widget.attrs['max'] = densidad_leche.max_value = producto.densidad_leche_max
        densidad_leche.label = f'Acidez de leche: (Norma {producto.densidad_leche_min} - {producto.densidad_leche_max})'
    
        proteina_leche = form.fields['proteina_leche']
        proteina_leche.widget.attrs['min'] = proteina_leche.min_value = producto.proteina_leche_min
        proteina_leche.widget.attrs['max'] = proteina_leche.max_value = producto.proteina_leche_max
        proteina_leche.label = f'Acidez de leche: (Norma {producto.proteina_leche_min} - {producto.proteina_leche_max})'
    
        acidez_mezcla = form.fields['acidez_mezcla']
        acidez_mezcla.widget.attrs['min'] = acidez_mezcla.min_value = producto.acidez_mezcla_min
        acidez_mezcla.widget.attrs['max'] = acidez_mezcla.max_value = producto.acidez_mezcla_max
        acidez_mezcla.label = f'Acidez de leche: (Norma {producto.acidez_mezcla_min} - {producto.acidez_mezcla_max})'
    
        materia_grasa_mezcla = form.fields['materia_grasa_mezcla']
        materia_grasa_mezcla.widget.attrs['min'] = materia_grasa_mezcla.min_value = producto.mg_mezcla_min
        materia_grasa_mezcla.widget.attrs['max'] = materia_grasa_mezcla.max_value = producto.mg_mezcla_max
        materia_grasa_mezcla.label = f'Acidez de leche: (Norma {producto.mg_mezcla_min} - {producto.mg_mezcla_max})'
    
        densidad_mezcla = form.fields['densidad_mezcla']
        densidad_mezcla.widget.attrs['min'] = densidad_mezcla.min_value = producto.densidad_mezcla_min
        densidad_mezcla.widget.attrs['max'] = densidad_mezcla.max_value = producto.densidad_mezcla_max
        densidad_mezcla.label = f'Acidez de leche: (Norma {producto.densidad_mezcla_min} - {producto.densidad_mezcla_max})'
    
        solidos_totales_mezcla = form.fields['solidos_totales_mezcla']
        solidos_totales_mezcla.widget.attrs['min'] = solidos_totales_mezcla.min_value = producto.solidos_totales_mezcla_min
        solidos_totales_mezcla.widget.attrs['max'] = solidos_totales_mezcla.max_value = producto.solidos_totales_mezcla_max
        solidos_totales_mezcla.label = f'Acidez de leche: (Norma {producto.solidos_totales_mezcla_min} - {producto.solidos_totales_mezcla_max})'
    
    data={'form':form}    
    return render(request, 'repo068/agregar.html', data)

@login_required
def repo068Eliminar(request, id):
    registro = get_object_or_404(DetalleRepo068, pk=id)
    registro.delete()
    return redirect('repo068_listar')

@login_required
def repo068Editar(request, id):
    registro = get_object_or_404(DetalleRepo068, pk=id)
    
    if request.method == 'POST':
        form=Repo068Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            return redirect('/repo068_listar')
    else:
        form=Repo068Form(instance=registro)
    data={'form':form}
    return render(request, 'repo068/editar.html', data)

@login_required
def estanqueFermentacionAgregar(request):
    nombre_modelo = EstanqueFermentacion.__name__
    form=EstanqueFermentacionForm()
    if request.method == 'POST':
        form=EstanqueFermentacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

@login_required
def estanqueLanzamientoAgregar(request):
    nombre_modelo = EstanqueLanzamiento.__name__
    form=EstanqueLanzamientoForm()
    if request.method == 'POST':
        form=EstanqueLanzamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    data={'form':form, 'nombre_modelo':nombre_modelo}
    return render(request, 'abstracto/agregarabstracto.html', data)

#-------------------------------------- Termino de los views para la RE PO 068 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 005 --------------------------------------

@login_required
def repo005Listar(request):
    repos005 = DetalleInsumosEnvasado.objects.order_by('-fecha')
    listaMateriaPrima = MateriaPrimaEnvasado.objects.all()
    
    paginator = Paginator(repos005, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)

    user = User.objects.get(username=request.user.username)
    groups = user.groups.all()
        
    data = {'repos005': objetos_pagina, 'page':page, 'listaMateriaPrima':listaMateriaPrima, 'groups':groups}
    return render(request, 'repo005/listar.html', data)

@login_required
def repo005Buscar(request):
    repos005 = DetalleInsumosEnvasado.objects.order_by('-fecha')
    listaMateriaPrima = MateriaPrimaEnvasado.objects.all()
    if request.method == "GET":
        query = request.GET.get('repo005_buscar')
        queryset = repos005.filter(Q(fecha__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos005 = paginator.page(page)
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all()
    
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos005':repos005,
            'listaMateriaPrima':listaMateriaPrima,
            'groups':groups
        }
        return render(request, 'repo005/buscar.html', data)

@login_required
def repo005Agregar(request):
    form=Repo005Form(request.POST or None)
    
    formMateriaPrima = formset_factory(MateriaPrimaEnvasadoForm, extra=1)
    
    if request.method == 'POST':
        
        formMateriaPrima = formMateriaPrima(request.POST)
        
        if form.is_valid() and formMateriaPrima.is_valid():
            obj2 = form.save(commit=False)
            obj2.usuario_del_registro = request.user.username
            obj2.save()
            for f in formMateriaPrima:
                if formMateriaPrima.is_valid():
                    obj = f.save(commit=False)
                    obj.detalle_insumo_envasado_id = form.instance.id
                    obj.save()
                    
            return redirect('/repo005_listar')
        
    data={'form':form, 'formMateriaPrima':formMateriaPrima}
    return render(request, 'repo005/agregar.html', data)

@login_required
def repo005Eliminar(request, id):
    registro = get_object_or_404(DetalleInsumosEnvasado, pk=id)
    registro.delete()
    return redirect('repo005_listar')

#Editar detalle de la formulación
@login_required
def repo005Editar(request, id):
    registro = get_object_or_404(DetalleInsumosEnvasado, pk=id)
    
    if request.method == 'POST':
        form=Repo005Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            return redirect('/repo005_listar')
    else:
        form=Repo005Form(instance=registro)
        
    data={'form':form}
    return render(request, 'repo005/editar.html', data)

#Editar una materia prima del detalle de la formulación
@login_required
def repo005Editar2(request, id):
    registro = get_object_or_404(MateriaPrimaEnvasado, pk=id)
    
    if request.method == 'POST':
        form=MateriaPrimaEnvasadoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('/repo005_listar')
    else:
        form=MateriaPrimaEnvasadoForm(instance=registro)
        
    data={'form':form}
    return render(request, 'repo005/editar2.html', data)

#-------------------------------------- Termino de los views para la RE PO 005 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para la RE PO 017 --------------------------------------

@login_required
def repo017Listar(request):
    repos017 = DetalleRepo017.objects.order_by('-fecha')
    listaMateriaPrima = MaterialEnvasado.objects.all()
    
    paginator = Paginator(repos017, 5)
    page = request.GET.get('page') or 1
    objetos_pagina = paginator.page(page)
    
    user = User.objects.get(username=request.user.username)
    groups = user.groups.all()

    data = {
        'repos017': objetos_pagina,
        'page':page,
        'listaMateriaPrima':listaMateriaPrima,
        'groups':groups,
        }
    return render(request, 'repo017/listar.html', data)

@login_required
def repo017Buscar(request):
    repos017 = DetalleRepo017.objects.order_by('-fecha')
    listaMateriaPrima = MaterialEnvasado.objects.all()
    if request.method == "GET":
        query = request.GET.get('repo017_buscar')
        queryset = repos017.filter(Q(fecha__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos017 = paginator.page(page)
        total = queryset.count()
        
        user = User.objects.get(username=request.user.username)
        groups = user.groups.all()
    
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos017':repos017,
            'listaMateriaPrima':listaMateriaPrima,
            'groups':groups
        }
        return render(request, 'repo017/buscar.html', data)

@login_required
def repo017Agregar(request):
    form=Repo017Form(request.POST or None)
    
    formMateriaPrima = formset_factory(MaterialEnvasadoForm, extra=1)
    
    if request.method == 'POST':
        
        formMateriaPrima = formMateriaPrima(request.POST)
        
        if form.is_valid() and formMateriaPrima.is_valid():
            obj2 = form.save(commit=False)
            obj2.usuario_del_registro = request.user.username
            obj2.save()
            for f in formMateriaPrima:
                if formMateriaPrima.is_valid():
                    obj = f.save(commit=False)
                    obj.detalle_repo017_id = form.instance.id
                    obj.save()
                    
            return redirect('/repo017_listar')
        
    data={'form':form, 'formMateriaPrima':formMateriaPrima}
    return render(request, 'repo017/agregar.html', data)

@login_required
def repo017Eliminar(request, id):
    registro = get_object_or_404(DetalleRepo017, pk=id)
    registro.delete()
    return redirect('repo017_listar')

#Editar detalle de la formulación
@login_required
def repo017Editar(request, id):
    registro = get_object_or_404(DetalleRepo017, pk=id)
    
    if request.method == 'POST':
        form=Repo017Form(request.POST, instance=registro)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_del_registro = request.user.username
            obj.save()
            return redirect('/repo017_listar')
    else:
        form=Repo017Form(instance=registro)
        
    data={'form':form}
    return render(request, 'repo017/editar.html', data)

#Editar una materia prima del detalle de la formulación
@login_required
def repo017Editar2(request, id):
    registro = get_object_or_404(MaterialEnvasado, pk=id)
    
    if request.method == 'POST':
        form=MaterialEnvasadoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('/repo017_listar')
    else:
        form=MaterialEnvasadoForm(instance=registro)
        
    data={'form':form}
    return render(request, 'repo017/editar2.html', data)

#-------------------------------------- Termino de los views para la RE PO 017 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los views para reportes --------------------------------------

@login_required 
def menuReporte(request):
    return render(request, 'reporte/menureportes.html')

@login_required
def buscarOp(request):
    repos003 = OrdenProceso.objects.order_by('-fecha')
    if request.method == "GET":
        query = request.GET.get('buscar_op')
        queryset = repos003.filter(Q(orden_proceso__icontains = query))
        
        paginator = Paginator(queryset, 1)
        page = request.GET.get('page') or 1
        repos003 = paginator.page(page)
        total = queryset.count()
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos003':repos003,
        }
        return render(request, 'reporte/buscar.html', data)
    
@login_required
def generarReporte(request, id):
    repo003 = get_object_or_404(OrdenProceso, pk=id)
    tlp = get_object_or_404(DetalleTlp, pk=repo003.tlp_id)
    repo013 = get_object_or_404(Detalle_pasteurizacion, pk=tlp.detalle_pasteurizacion_id)
    tlc = get_object_or_404(DetalleTlc, pk=repo013.tlc_id)
    repo001 = get_object_or_404(DetalleCamionRecepcionLeche, pk=tlc.detalle_camion_recepcion_leche_id)
    repo004 = DetalleInsumosFormulacion.objects.filter(orden_proceso_id = repo003.id)
    listaMateriaPrima = MateriaPrima.objects.all()
    repo068 = DetalleRepo068.objects.filter(orden_proceso_id = repo003.id)
    repo005 = DetalleInsumosEnvasado.objects.filter(orden_proceso_id = repo003.id)
    listaMateriaPrimaEnvasado = MateriaPrimaEnvasado.objects.all()
    repo017 = DetalleRepo017.objects.filter(orden_proceso_id = repo003.id)
    listaMaterialEnvasado = MaterialEnvasado.objects.all()
    
    data={
        'repo003':repo003,
        'tlp':tlp,
        'repo013':repo013,
        'tlc':tlc,
        'repo001':repo001,
        'repo004':repo004,
        'listaMateriaPrima':listaMateriaPrima,
        'repo068':repo068,
        'repo005':repo005,
        'listaMateriaPrimaEnvasado':listaMateriaPrimaEnvasado,
        'repo017':repo017,
        'listaMaterialEnvasado':listaMaterialEnvasado,
        }
    return render(request, 'reporte/trazabilidad.html', data)


@login_required
def buscarFermento(request):
    repos068 = DetalleRepo068.objects.order_by('fermento')
    
    if request.method == "GET":
        query1 = request.GET.get('buscar_fermento')
        query2 = request.GET.get('buscar_lote')
        queryset = repos068.filter(Q(fermento__icontains = query1) & Q(fermento_lote__icontains = query2))
        
        repos003 = OrdenProceso.objects.all()
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos068 = paginator.page(page)
        total = queryset.count()
        
        data = {
            'page':page,
            'total':total,
            'query':query1,
            'query2':query2,
            'repos068':repos068,
            'repos003':repos003,
        }
        return render(request, 'reporte/buscarfermento.html', data)

@login_required
def buscarRecorrido(request):
    repos001 = DetalleCamionRecepcionLeche.objects.order_by('numero_guia')
    
    if request.method == "GET":
        query = request.GET.get('buscar_recorrido')
        queryset = repos001.filter(Q(numero_guia__icontains = query))
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page') or 1
        repos001 = paginator.page(page)
        total = queryset.count()
        
        
        data = {
            'page':page,
            'total':total,
            'query':query,
            'repos001':repos001,
        }
        return render(request, 'reporte/buscarrecorrido.html', data)
    
@login_required
def buscarRecorrido2(request, id):
    repo001 = get_object_or_404(DetalleCamionRecepcionLeche, pk=id)
    
    detalleTlc = DetalleTlc.objects.all()
    repos013 = Detalle_pasteurizacion.objects.all()
    detalleTlp = DetalleTlp.objects.all()
    repos003 = OrdenProceso.objects.all()
    
    data={
        'repo001':repo001,
        'detalleTlc':detalleTlc,
        'repos013':repos013,
        'detalleTlp':detalleTlp,
        'repos003':repos003,
        }
    return render(request, 'reporte/buscarrecorrido2.html', data)