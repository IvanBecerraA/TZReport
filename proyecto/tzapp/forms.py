from django import forms
from tzapp.models import *

#-------------------------------------- Inicio de los forms para la RE PO 001 --------------------------------------
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
    class Meta:
        model=DetalleCamionRecepcionLeche
        fields = '__all__'
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
    """ operador = forms.ForeignKey(Operador, on_delete=forms.SET_NULL, null = True)
    placa = forms.ForeignKey(Camion, on_delete=forms.SET_NULL, null = True)
    recorrido = forms.ForeignKey(Recorrido, on_delete=forms.SET_NULL, null = True) """
    numero_guia = forms.IntegerField()
    sello = forms.CharField(widget=forms.Textarea, label='Sello: separar con la tecla ENTER')
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
    """ tlc = forms.ManyToManyField(Tlc, through= 'DetalleTlc') """
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
    """ operador = forms.ForeignKey(Operador, on_delete=forms.SET_NULL, null = True)
    placa = forms.ForeignKey(Camion, on_delete=forms.SET_NULL, null = True)
    recorrido = forms.ForeignKey(Recorrido, on_delete=forms.SET_NULL, null = True) """
    numero_guia.widget.attrs['class']='form-control'
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
    """ tlc = forms.ManyToManyField(Tlc, through= 'DetalleTlc') """
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
    