from django import forms
from tzapp.models import *

#-------------------------------------- Inicio de los forms para la RE PO 001 --------------------------------------
parametrosRepo001Lista = parametrosRepo001.objects.get(pk = 1)

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
    temperatura_leche_guia = forms.FloatField(
        min_value=parametrosRepo001Lista.temperatura_leche_guia_minimo,
        max_value=parametrosRepo001Lista.temperatura_leche_guia_maximo,
        label=f'Temperatura leche guía: (Norma {parametrosRepo001Lista.temperatura_leche_guia_minimo} - {parametrosRepo001Lista.temperatura_leche_guia_maximo})')
    temperatura_leche_pool = forms.FloatField(
        min_value=parametrosRepo001Lista.temperatura_leche_pool_minimo, 
        max_value=parametrosRepo001Lista.temperatura_leche_pool_maximo, 
        label=f'Temperatura leche pool: (Norma {parametrosRepo001Lista.temperatura_leche_pool_minimo} - {parametrosRepo001Lista.temperatura_leche_pool_maximo})')
    temperatura_leche_salida_enfriador = forms.FloatField(
        min_value=parametrosRepo001Lista.temperatura_leche_salida_enfriador_minimo, 
        max_value=parametrosRepo001Lista.temperatura_leche_salida_enfriador_maximo, 
        label=f'Temperatura leche salida enfriador: (Norma {parametrosRepo001Lista.temperatura_leche_salida_enfriador_minimo} - {parametrosRepo001Lista.temperatura_leche_salida_enfriador_maximo})')
    litros_camion = forms.FloatField()
    kilo_gramos_camion = forms.FloatField()
    litros_sap = forms.IntegerField()
    acidez = forms.FloatField(
        min_value=parametrosRepo001Lista.acidez_minimo, 
        max_value=parametrosRepo001Lista.acidez_maximo, 
        label=f'Acidez: (Norma {parametrosRepo001Lista.acidez_minimo} - {parametrosRepo001Lista.acidez_maximo})')
    ph_camion = forms.FloatField(
        min_value=parametrosRepo001Lista.ph_camion_minimo, 
        max_value=parametrosRepo001Lista.ph_camion_maximo, 
        label=f'PH: (Norma {parametrosRepo001Lista.ph_camion_minimo} - {parametrosRepo001Lista.ph_camion_maximo})')
    prueba = forms.FloatField(
        min_value=parametrosRepo001Lista.prueba_minimo, 
        max_value=parametrosRepo001Lista.prueba_maximo, 
        label=f'Prueba: (Norma {parametrosRepo001Lista.prueba_minimo} - {parametrosRepo001Lista.prueba_maximo})')
    snap = forms.CharField(widget=forms.Select(choices=Snaps))
    mg = forms.FloatField(
        min_value=parametrosRepo001Lista.mg_minimo, 
        max_value=parametrosRepo001Lista.mg_maximo, 
        label=f'MG: (Norma {parametrosRepo001Lista.mg_minimo} - {parametrosRepo001Lista.mg_maximo})')
    sng = forms.FloatField(
        min_value=parametrosRepo001Lista.sng_minimo, 
        max_value=parametrosRepo001Lista.sng_maximo, 
        label=f'SNG: (Norma {parametrosRepo001Lista.sng_minimo} - {parametrosRepo001Lista.sng_maximo})')
    st = forms.FloatField(
        min_value=parametrosRepo001Lista.st_minimo, 
        max_value=parametrosRepo001Lista.st_maximo, 
        label=f'ST: (Norma {parametrosRepo001Lista.st_minimo} - {parametrosRepo001Lista.st_maximo})')
    proteina = forms.FloatField(
        min_value=parametrosRepo001Lista.proteina_minimo, 
        max_value=parametrosRepo001Lista.proteina_maximo, 
        label=f'Proteina: (Norma {parametrosRepo001Lista.proteina_minimo} - {parametrosRepo001Lista.proteina_maximo})')
    densidad = forms.FloatField(
        min_value=parametrosRepo001Lista.densidad_minimo, 
        max_value=parametrosRepo001Lista.densidad_maximo, 
        label=f'Densidad: (Norma {parametrosRepo001Lista.densidad_minimo} - {parametrosRepo001Lista.densidad_maximo})')
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
#-------------------------------------- Fin de los modelos para la RE PO 001 --------------------------------------



#-------------------------------------- Inicio de los forms para la RE PO 013 --------------------------------------

class Repo013Form(forms.ModelForm):
    class Meta: #metadatos
        model= Detalle_pasteurizacion
        fields = '__all__'
        
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
    
    fecha_registro.widget.attrs['class']='form-control'
    litros_salida_tlp.widget.attrs['class']='form-control'
    saldo.widget.attrs['class']='form-control'
    tipo_leche.widget.attrs['class']='form-control'
    observacion.widget.attrs['class']='form-control'
    fecha_pasteurizacion.widget.attrs['class']='form-control'
    hora_inicio.widget.attrs['class']='form-control'
    hora_termino.widget.attrs['class']='form-control'
    temperatura_salida_pasteurizador.widget.attrs['class']='form-control'
    
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
    
#-------------------------------------- Fin de los modelos para la RE PO 013 --------------------------------------
