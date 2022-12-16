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
    fecha_y_hora_estandarizacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tlc} :{self.fecha_y_hora_estandarizacion}'
    
class parametrosRepo001(models.Model):
    temperatura_leche_guia_minimo = models.FloatField()
    temperatura_leche_guia_maximo = models.FloatField()
    temperatura_leche_pool_minimo = models.FloatField()
    temperatura_leche_pool_maximo = models.FloatField()
    temperatura_leche_salida_enfriador_minimo = models.FloatField()
    temperatura_leche_salida_enfriador_maximo = models.FloatField()
    acidez_minimo = models.FloatField()
    acidez_maximo = models.FloatField()
    ph_camion_minimo = models.FloatField()
    ph_camion_maximo = models.FloatField()
    prueba_minimo = models.FloatField()
    prueba_maximo = models.FloatField()
    mg_minimo = models.FloatField()
    mg_maximo = models.FloatField()
    sng_minimo = models.FloatField()
    sng_maximo = models.FloatField()
    st_minimo = models.FloatField()
    st_maximo = models.FloatField()
    proteina_minimo = models.FloatField()
    proteina_maximo = models.FloatField()
    densidad_minimo = models.FloatField()
    densidad_maximo = models.FloatField()

#-------------------------------------- Fin de los modelos para la RE PO 001 --------------------------------------



#-------------------------------------- Inicio de los modelos para la RE PO 013 --------------------------------------

class Tct(models.Model):
    nombre = models.CharField(max_length=25)
    
    def __str__(self):
        return f'{self.nombre}'
    
class Tlp(models.Model):
    nombre = models.CharField(max_length=25)
        
    def __str__(self):
        return f'{self.nombre}'
    
class Detalle_pasteurizacion(models.Model):
    tlc = models.ForeignKey(DetalleTlc, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    tct = models.ForeignKey(Tct, on_delete=models.CASCADE)
    tlp = models.ManyToManyField(Tlp, through= 'DetalleTlp')
    fecha_registro = models.DateField()
    litros_salida_tlp = models.IntegerField()
    saldo= models.IntegerField()
    tipo_leche= models.CharField(max_length=30) 
    observacion = models.CharField(max_length=30)
    fecha_pasteurizacion = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    temperatura_salida_pasteurizador = models.FloatField()

class DetalleTlp(models.Model):
    tlp = models.ForeignKey(Tlp, on_delete=models.CASCADE)
    detalle_pasteurizacion = models.ForeignKey(Detalle_pasteurizacion, on_delete=models.CASCADE)
    fecha_y_hora_estandarizacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.tlp} :{self.fecha_y_hora_estandarizacion}'

#-------------------------------------- Fin de los modelos para la RE PO 013 --------------------------------------



#-------------------------------------- Fin de los modelos para la RE PO 003 --------------------------------------

#-------------------------------------- Fin de los modelos para la RE PO 003 --------------------------------------
