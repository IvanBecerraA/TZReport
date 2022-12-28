from django import forms
from tzapp.models import *

#-------------------------------------- Inicio de los forms para la RE PO 001 --------------------------------------
""" parametrosRepo001Lista = parametrosRepo001.objects.get(pk = 1) """

class CamionForm(forms.ModelForm):
    class Meta:
        model=Camion
        fields = '__all__'
    placa = forms.CharField()
    
    placa.widget.attrs['class']='form-control'
    
class RecorridoForm(forms.ModelForm):
    class Meta:
        model=Recorrido
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
    
class OperadorForm(forms.ModelForm):
    class Meta:
        model=Operador
        fields = '__all__'
    nombre = forms.CharField()
    apellido = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
    apellido.widget.attrs['class']='form-control'

class TlcForm(forms.ModelForm):
    class Meta:
        model=Tlc
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
    
class Repo001Form(forms.ModelForm):
    class Meta: # Metadatos necesarios para el formulario
        model=DetalleCamionRecepcionLeche #Modelo a utilizar para el formulario
        fields = '__all__' # Añadir todos los campos al formulario
        exclude = ['usuario_del_registro'] # Excluir campo en el formulario
        
    ColoresYOlores = [
        ('normal', 'NORMAL'),
        ('anormal', 'ANORMAL'),
    ]
    Snaps = [
        ('negativo', 'NEGATIVO'),
        ('positivo', 'POSITIVO'),
    ]
    TiposDeAseos = [
        ('enjuague', 'ENJUAGUE'),
        ('enjuague mas sanitizado', 'ENJUAGUE MAS SANITIZADO'),
        ('sanitizado', 'SANITIZADO'),
        ('aseo', 'ASEO'),
    ]
    
    fecha = forms.DateField(widget=forms.DateInput)
    numero_guia = forms.IntegerField()
    sello = forms.CharField(widget=forms.Textarea, label='Sello: separar con la tecla coma ( , )')
    temperatura_leche_guia = forms.FloatField()
    temperatura_leche_pool = forms.FloatField()
    temperatura_leche_salida_enfriador = forms.FloatField()
    litros_camion = forms.FloatField()
    kilo_gramos_camion = forms.FloatField()
    litros_sap = forms.IntegerField()
    acidez = forms.FloatField()
    ph_camion = forms.FloatField()
    prueba = forms.FloatField()
    snap = forms.CharField(widget=forms.Select(choices=Snaps))
    mg = forms.FloatField()
    sng = forms.FloatField()
    st = forms.FloatField()
    proteina = forms.FloatField()
    densidad = forms.FloatField()
    color_y_olor = forms.CharField(widget=forms.Select(choices=ColoresYOlores))
    hora_ingreso_a_planta = forms.TimeField(widget=forms.TimeInput)
    hora_muestra = forms.TimeField(widget=forms.TimeInput)
    hora_inicio_descarga = forms.TimeField(widget=forms.TimeInput)
    hora_termino_descarga = forms.TimeField(widget=forms.TimeInput)
    hora_inicio_aseo = forms.TimeField(widget=forms.TimeInput)
    hora_termino_aseo = forms.TimeField(widget=forms.TimeInput)
    hora_salida_planta = forms.TimeField(widget=forms.TimeInput)
    kilo_gramos_camion_salida = forms.FloatField()
    tipo_aseo_camion = forms.CharField(widget=forms.Select(choices=TiposDeAseos))
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha.widget.attrs['class']='form-control'
    sello.widget.attrs['class']='form-control'
    temperatura_leche_guia.widget.attrs['class']='form-control'
    temperatura_leche_pool.widget.attrs['class']='form-control'
    temperatura_leche_salida_enfriador.widget.attrs['class']='form-control'
    litros_camion.widget.attrs['class']='form-control'
    kilo_gramos_camion.widget.attrs['class']='form-control'
    litros_sap.widget.attrs['class']='form-control'
    acidez.widget.attrs['class']='form-control'
    ph_camion.widget.attrs['class']='form-control'
    prueba.widget.attrs['class']='form-control'
    snap.widget.attrs['class']='form-control'
    mg.widget.attrs['class']='form-control'
    sng.widget.attrs['class']='form-control'
    st.widget.attrs['class']='form-control'
    proteina.widget.attrs['class']='form-control'
    densidad.widget.attrs['class']='form-control'
    color_y_olor.widget.attrs['class']='form-control'
    hora_ingreso_a_planta.widget.attrs['class']='form-control'
    hora_muestra.widget.attrs['class']='form-control'
    hora_inicio_descarga.widget.attrs['class']='form-control'
    hora_termino_descarga.widget.attrs['class']='form-control'
    hora_inicio_aseo.widget.attrs['class']='form-control'
    hora_termino_aseo.widget.attrs['class']='form-control'
    hora_salida_planta.widget.attrs['class']='form-control'
    kilo_gramos_camion_salida.widget.attrs['class']='form-control'
    tipo_aseo_camion.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
#-------------------------------------- Termino de los modelos para la RE PO 001 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los forms para la RE PO 013 --------------------------------------
    
class TctForm(forms.ModelForm):
    class Meta:
        model=Tct
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
        
class TlpForm(forms.ModelForm):
    class Meta:
        model=Tlp
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'

class Repo013Form(forms.ModelForm):
    class Meta: #metadatos
        model= Detalle_pasteurizacion
        fields = '__all__'
        exclude = ['usuario_del_registro']
        
    TiposLeches = [
        ('entera', 'ENTERA'),
        ('descremada', 'DESCREMADA'),       
    ]
    Observaciones = [
        ('no se vacia', 'NO SE VACIA'),
        ('vacio', 'VACIO'),
        ('aseo', 'ASEO'),
        ('vacio y aseo', 'VACIO Y ASEO'),
     ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Obtener los datos de DetalleTLC ordenados de forma descendente por su fecha de creación, para ordenarlos en el campo tlc mostrando los nuevos primero
        self.fields['tlc'].queryset = DetalleTlc.objects.all().order_by('-fecha_creacion')
    
    fecha_registro = forms.DateField(widget=forms.DateInput) #valida que se ingrese una fecha
    litros_salida_tlp = forms.IntegerField()
    saldo= forms.IntegerField()
    tipo_leche= forms.CharField(widget=forms.Select(choices=TiposLeches))
    observacion = forms.CharField(widget=forms.Select(choices=Observaciones))
    fecha_pasteurizacion = forms.DateField(widget=forms.DateInput)
    hora_inicio = forms.TimeField(widget=forms.TimeInput)
    hora_termino = forms.TimeField(widget=forms.TimeInput)
    temperatura_salida_pasteurizador = forms.FloatField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha_registro.widget.attrs['class']='form-control'
    litros_salida_tlp.widget.attrs['class']='form-control'
    saldo.widget.attrs['class']='form-control'
    tipo_leche.widget.attrs['class']='form-control'
    observacion.widget.attrs['class']='form-control'
    fecha_pasteurizacion.widget.attrs['class']='form-control'
    hora_inicio.widget.attrs['class']='form-control'
    hora_termino.widget.attrs['class']='form-control'
    temperatura_salida_pasteurizador.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
    
#-------------------------------------- Termino de los modelos para la RE PO 013 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los modelos para la RE PO 003 --------------------------------------

class TmyForm(forms.ModelForm):
    class Meta:
        model=Tmy
        fields = '__all__'
    
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'

class MaquinaForm(forms.ModelForm):
    class Meta:
        model=Maquina
        fields = '__all__'
    
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
    
class Repo003Form(forms.ModelForm):
    class Meta:
        model=OrdenProceso
        fields = '__all__'
        exclude = ['usuario_del_registro']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tlp'].queryset = DetalleTlp.objects.all().order_by('-fecha_creacion')
        
    orden_proceso = forms.IntegerField()
    orden_proceso_base_blanca = forms.IntegerField()
    sabor = forms.CharField()
    litros = forms.FloatField()
    fecha = forms.DateField(widget=forms.DateInput)
    hora = forms.TimeField(widget=forms.TimeInput)
    operador_pasteurizacion = forms.CharField()
    operador_fermentacion = forms.CharField()
    operador_dosimetria = forms.CharField()
    cantidad_tlp = forms.FloatField()
    cantidad_crema= forms.FloatField()
    litros_agua = forms.FloatField()
    litros_total_llenado = forms.FloatField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    orden_proceso.widget.attrs['class']='form-control'
    orden_proceso_base_blanca.widget.attrs['class']='form-control'
    sabor.widget.attrs['class']='form-control'
    litros.widget.attrs['class']='form-control'
    fecha.widget.attrs['class']='form-control'
    hora.widget.attrs['class']='form-control'
    operador_pasteurizacion.widget.attrs['class']='form-control'
    operador_fermentacion.widget.attrs['class']='form-control'
    operador_dosimetria.widget.attrs['class']='form-control'
    cantidad_tlp.widget.attrs['class']='form-control'
    cantidad_crema.widget.attrs['class']='form-control'
    litros_agua.widget.attrs['class']='form-control'
    litros_total_llenado.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
    
#-------------------------------------- Termino de los modelos para la RE PO 003 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los modelos para la RE PO 004 --------------------------------------

class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = '__all__'
        exclude = ['detalle_pasteurizacion']
        
    nombre = forms.CharField()
    kilos = forms.IntegerField()
    lote = forms.CharField()
    fecha_vencimiento = forms.DateField(widget=forms.DateInput)
    
    nombre.widget.attrs['class']='form-control'
    kilos.widget.attrs['class']='form-control'
    lote.widget.attrs['class']='form-control'
    fecha_vencimiento.widget.attrs['class']='form-control'
    
    
class Repo004Form(forms.ModelForm):
    class Meta:
        model = DetalleInsumosFormulacion
        fields = '__all__'
        exclude = ['usuario_del_registro']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_proceso'].queryset = OrdenProceso.objects.all().order_by('-orden_proceso')
    
    fecha_fabricacion = forms.DateField(widget=forms.DateInput)
    hora_fabricacion = forms.TimeField(widget=forms.TimeInput)
    fecha_formulacion = forms.DateField(widget=forms.DateInput)
    hora_formulacion = forms.TimeField(widget=forms.TimeInput)
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha_fabricacion.widget.attrs['class']='form-control'
    hora_fabricacion.widget.attrs['class']='form-control'
    fecha_formulacion.widget.attrs['class']='form-control'
    hora_formulacion.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
    
#-------------------------------------- Termino de los modelos para la RE PO 004 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los modelos para la RE PO 068 --------------------------------------


class EstanqueFermentacionForm(forms.ModelForm):
    class Meta:
        model=EstanqueFermentacion
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'

class EstanqueLanzamientoForm(forms.ModelForm):
    class Meta:
        model=EstanqueLanzamiento
        fields = '__all__'
    nombre = forms.CharField()
    
    nombre.widget.attrs['class']='form-control'
    
    
class Repo068Form(forms.ModelForm):
    class Meta:
        model = DetalleRepo068
        fields = '__all__'
        exclude = ['usuario_del_registro']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_proceso'].queryset = OrdenProceso.objects.all().order_by('-orden_proceso')
    
    Cumple = [
        ('ok', 'OK'),
        ('no cumple', 'NO CUMPLE'),
    ]
    Revision = [
        ('produccion', 'PRODUCCION'),
        ('cumple', 'CUMPLE'),
    ]    
    Estado = [
        ('no', 'NO'),
        ('si', 'SI'),
    ]
    
    fecha_estandarizacion = forms.DateField(widget=forms.DateInput)
    hora_estandarizacion = forms.TimeField(widget=forms.TimeInput)
    acidez_leche = forms.FloatField()
    temperatura_leche = forms.FloatField()
    materia_grasa_leche = forms.FloatField()
    densidad_leche = forms.FloatField()
    proteina_leche = forms.FloatField()
    operador_muestra_leche = forms.CharField()
    acidez_mezcla = forms.FloatField()
    temperatura_mezcla = forms.FloatField()
    materia_grasa_mezcla = forms.FloatField()
    densidad_mezcla = forms.FloatField()
    solidos_totales_mezcla = forms.FloatField()
    operador_muestra_mezcla = forms.CharField()
    filtro_pasteurizador = forms.CharField(widget=forms.Select(choices=Cumple))
    filtro_311 = forms.CharField(widget=forms.Select(choices=Revision))
    filtro_312 = forms.CharField(widget=forms.Select(choices=Revision))
    filtro_313 = forms.CharField(widget=forms.Select(choices=Revision))
    filtro_314 = forms.CharField(widget=forms.Select(choices=Revision))
    filtro_316 = forms.CharField(widget=forms.Select(choices=Revision))
    hora_inicio_pasteurizacion = forms.TimeField(widget=forms.TimeInput)
    hora_adicion_fermentos = forms.TimeField(widget=forms.TimeInput)
    fermento = forms.CharField()
    fermento_lote = forms.CharField()
    temperatura_pasteurizador = forms.FloatField()
    presion_pasteurizador = forms.FloatField()
    hora_termino_pasteurizacion = forms.TimeField(widget=forms.TimeInput)
    litros_pasteurizados = forms.FloatField()
    ph_corte = forms.FloatField()
    tiempo_fermentacion = forms.TimeField(widget=forms.TimeInput)
    inicio_enfriamiento = forms.TimeField(widget=forms.TimeInput)
    termino_enfriamiento = forms.TimeField(widget=forms.TimeInput)
    tiempo_enfriamiento = forms.TimeField(widget=forms.TimeInput)
    presion_enfriamiento = forms.FloatField()
    ystral_enfriamiento = forms.IntegerField()
    viscosidad = forms.IntegerField()    
    grumos = forms.CharField(widget=forms.Select(choices=Estado))
    espuma = forms.CharField(widget=forms.Select(choices=Estado))
    desuerado = forms.CharField(widget=forms.Select(choices=Estado))
    sabor = forms.CharField(widget=forms.Select(choices=Cumple))
    temperatura_frio = forms.FloatField()
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha_estandarizacion.widget.attrs['class']='form-control'
    hora_estandarizacion.widget.attrs['class']='form-control'
    acidez_leche.widget.attrs['class']='form-control'
    temperatura_leche.widget.attrs['class']='form-control'
    materia_grasa_leche.widget.attrs['class']='form-control'
    densidad_leche.widget.attrs['class']='form-control'
    proteina_leche.widget.attrs['class']='form-control'
    operador_muestra_leche.widget.attrs['class']='form-control'
    acidez_mezcla.widget.attrs['class']='form-control'
    temperatura_mezcla.widget.attrs['class']='form-control'
    materia_grasa_mezcla.widget.attrs['class']='form-control'
    densidad_mezcla.widget.attrs['class']='form-control'
    solidos_totales_mezcla.widget.attrs['class']='form-control'
    operador_muestra_mezcla.widget.attrs['class']='form-control'
    filtro_pasteurizador.widget.attrs['class']='form-control'
    filtro_311.widget.attrs['class']='form-control'
    filtro_312.widget.attrs['class']='form-control'
    filtro_313.widget.attrs['class']='form-control'
    filtro_314.widget.attrs['class']='form-control'
    filtro_316.widget.attrs['class']='form-control'
    hora_inicio_pasteurizacion.widget.attrs['class']='form-control'
    hora_adicion_fermentos.widget.attrs['class']='form-control'
    fermento.widget.attrs['class']='form-control'
    fermento_lote.widget.attrs['class']='form-control'
    temperatura_pasteurizador.widget.attrs['class']='form-control'
    presion_pasteurizador.widget.attrs['class']='form-control'
    hora_termino_pasteurizacion.widget.attrs['class']='form-control'
    litros_pasteurizados.widget.attrs['class']='form-control'
    ph_corte.widget.attrs['class']='form-control'
    tiempo_fermentacion.widget.attrs['class']='form-control'
    inicio_enfriamiento.widget.attrs['class']='form-control'
    termino_enfriamiento.widget.attrs['class']='form-control'
    tiempo_enfriamiento.widget.attrs['class']='form-control'
    presion_enfriamiento.widget.attrs['class']='form-control'
    ystral_enfriamiento.widget.attrs['class']='form-control'
    viscosidad.widget.attrs['class']='form-control'
    grumos.widget.attrs['class']='form-control'
    espuma.widget.attrs['class']='form-control'
    desuerado.widget.attrs['class']='form-control'
    sabor.widget.attrs['class']='form-control'
    temperatura_frio.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
    
    
#-------------------------------------- Termino de los modelos para la RE PO 068 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los modelos para la RE PO 005 --------------------------------------

class MateriaPrimaEnvasadoForm(forms.ModelForm):
    class Meta:
        model = MateriaPrimaEnvasado
        fields = '__all__'
        exclude = ['detalle_insumo_envasado']
        
    nombre = forms.CharField()
    kilos_consumo = forms.IntegerField()
    lote = forms.CharField()
    numero_contenedor = forms.IntegerField()
    numero_usos = forms.IntegerField()
    fecha_vencimiento = forms.DateField(widget=forms.DateInput)
    hora_uso = forms.TimeField(widget=forms.TimeInput)
        
    nombre.widget.attrs['class']='form-control'
    kilos_consumo.widget.attrs['class']='form-control'
    lote.widget.attrs['class']='form-control'
    numero_contenedor.widget.attrs['class']='form-control'
    numero_usos.widget.attrs['class']='form-control'
    fecha_vencimiento.widget.attrs['class']='form-control'
    hora_uso.widget.attrs['class']='form-control'
    
class Repo005Form(forms.ModelForm):
    class Meta:
        model = DetalleInsumosEnvasado
        fields = '__all__'
        exclude = ['usuario_del_registro']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_proceso'].queryset = OrdenProceso.objects.all().order_by('-orden_proceso')
    
    fecha = forms.DateField(widget=forms.DateInput)
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'
    
#-------------------------------------- Termino de los modelos para la RE PO 005 --------------------------------------
#
#
#
#-------------------------------------- Inicio de los modelos para la RE PO 017 --------------------------------------

class MaterialEnvasadoForm(forms.ModelForm):
    class Meta:
        model = MaterialEnvasado
        fields = '__all__'
        exclude = ['detalle_repo017']
    
    Material = [
        ('rollos pai', 'ROLLOS PAI'),
        ('rollos decor', 'ROLLOS DECOR'),
        ('rollos tapa', 'ROLLOS TAPA'),
    ]
        
    nombre = forms.CharField(widget=forms.Select(choices=Material))
    kilos_consumo = forms.IntegerField()
    lote = forms.CharField()
    fecha_elaboracion = forms.DateField(widget=forms.DateInput)
        
    nombre.widget.attrs['class']='form-control'
    kilos_consumo.widget.attrs['class']='form-control'
    lote.widget.attrs['class']='form-control'
    fecha_elaboracion.widget.attrs['class']='form-control'

class Repo017Form(forms.ModelForm):
    class Meta:
        model = DetalleRepo017
        fields = '__all__'
        exclude = ['usuario_del_registro']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden_proceso'].queryset = OrdenProceso.objects.all().order_by('-orden_proceso')
    
    fecha = forms.DateField(widget=forms.DateInput)
    comentario = forms.CharField(required=False, widget=forms.Textarea)
    
    fecha.widget.attrs['class']='form-control'
    comentario.widget.attrs['class']='form-control'

#-------------------------------------- Termino de los modelos para la RE PO 017 --------------------------------------
