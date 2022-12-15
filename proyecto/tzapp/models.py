from django.db import models

# Create your models here.
#-------------------------------------- Inicio de los modelos para la RE PO 001 --------------------------------------
class Camion(models.Model):
    placa = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.placa}'
    
class Recorrido(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'
    
class Operador(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'    
    
class Tlc(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nombre}'
    
class DetalleCamionRecepcionLeche(models.Model):
    fecha = models.DateField()
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    placa = models.ForeignKey(Camion, on_delete=models.CASCADE)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE)
    tlc = models.ManyToManyField(Tlc, through= 'DetalleTlc')
    numero_guia = models.IntegerField()
    sello = models.CharField(max_length=100)
    temperatura_leche_guia = models.FloatField()
    temperatura_leche_pool = models.FloatField()
    temperatura_leche_salida_enfriador = models.FloatField()
    litros_camion = models.FloatField()
    kilo_gramos_camion = models.FloatField()
    litros_sap = models.IntegerField()
    acidez = models.FloatField()
    ph_camion = models.FloatField()
    prueba = models.FloatField()
    snap = models.CharField(max_length=20)
    mg = models.FloatField()
    sng = models.FloatField()
    st = models.FloatField()
    proteina = models.FloatField()
    densidad = models.FloatField()
    color_y_olor = models.CharField(max_length=30)
    hora_ingreso_a_planta = models.TimeField()
    hora_muestra = models.TimeField()
    hora_inicio_descarga = models.TimeField()
    hora_termino_descarga = models.TimeField()
    hora_inicio_aseo = models.TimeField()
    hora_termino_aseo = models.TimeField()
    hora_salida_planta = models.TimeField()
    kilo_gramos_camion_salida = models.FloatField()
    tipo_aseo_camion = models.CharField(max_length=30)
    comentario = models.CharField(max_length=100, null = True)
    
    def __str__(self):
        return f'{self.numero_guia}'
    
class DetalleTlc(models.Model):
    tlc = models.ForeignKey(Tlc, on_delete=models.CASCADE)
    detalle_camion_recepcion_leche = models.ForeignKey(DetalleCamionRecepcionLeche, on_delete=models.CASCADE)
    """ vacio = models.CharField(max_length=20) """
    hora_estandarizacion = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tlc} :{self.hora_estandarizacion}'

#-------------------------------------- Fin de los modelos para la RE PO 001 --------------------------------------

    