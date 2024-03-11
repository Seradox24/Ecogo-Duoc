from django.core.validators import MaxValueValidator
from django.db import models
from core.models import *


class Situacion(models.Model):
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado

class DiaSemana(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class ExpAprendizaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion

class Semaforo(models.Model):
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado

class SalidaTerreno(models.Model):
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE)
    numero_cuenta = models.IntegerField()
    semestre = models.CharField(max_length=100,blank=True, null=True)
    anio = models.PositiveIntegerField(validators=[MaxValueValidator(3000)],blank=True, null=True)
    semana = models.PositiveIntegerField(validators=[MaxValueValidator(3000)],blank=True, null=True)
    diasemana =  models.ManyToManyField(DiaSemana, blank=True,)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE,blank=True, null=True)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    dias = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    noches = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    lugar_ejecucion = models.CharField(max_length=60)
    asignaturas = models.ManyToManyField(Asignatura, related_name='salidas_terreno',blank=True)
    exp_aprendizaje = models.ForeignKey(ExpAprendizaje, on_delete=models.CASCADE, blank=True, null=True)
    num_alumnos = models.PositiveIntegerField(validators=[MaxValueValidator(150)], blank=True, null=True)
    #secciones = models.ManyToManyField(Seccion, through='SalidaSeccion',blank=True)
    secciones = models.ManyToManyField(Seccion,blank=True)
    docente_titular = models.ForeignKey(UsersMetadata, on_delete=models.CASCADE, related_name='salidas_terreno_titular',  blank=True, null=True)
    docentes_apoyo = models.ManyToManyField(UsersMetadata, related_name='salidas_terreno_apoyo',  blank=True)
    num_salida = models.IntegerField(validators=[MaxValueValidator(999)])
    asig_comp_terreno = models.ManyToManyField(Asignatura, related_name='salidas_terreno_asig_comp_terreno', blank=True)
    observaciones = models.TextField()
    semaforo = models.ForeignKey(Semaforo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        asignaturas_str = ', '.join([asignatura.nombre for asignatura in self.asignaturas.all()])
        return f"Salida a terreno de {asignaturas_str} - {self.fecha_ingreso}"

    class Meta:
        verbose_name = 'Salida Terreno'
        verbose_name_plural = 'Salidas Terreno'
 






class PronosticoClima(models.Model):
    salida_terreno = models.ForeignKey(SalidaTerreno, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=100, null=True, blank=True)  # Sin valor predeterminado
    region = models.CharField(max_length=100, default="sin informacion", null=True, blank=True)
    pais = models.CharField(max_length=100, default="sin informacion", null=True, blank=True)
    temperatura_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperatura_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    uv_index = models.IntegerField(null=True, blank=True)
    probabilidad_lluvia = models.IntegerField(null=True, blank=True)
    condiciones = models.CharField(max_length=100, null=True, blank=True)
    icono = models.URLField(null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)# Campo para la fecha y hora de la última actualización
    ultima_actualizacion_api = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pronóstico para {self.ubicacion} - {self.fecha} - {self.salida_terreno} "

    class Meta:
        verbose_name = 'Pronóstico Clima'
        verbose_name_plural = 'Pronósticos Clima'
        unique_together = ['salida_terreno', 'fecha']


class CurrentClima(models.Model):
    salida_terreno = models.ForeignKey(SalidaTerreno, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100,null=True, blank=True)
    region = models.CharField(max_length=100,null=True, blank=True)
    pais = models.CharField(max_length=100,null=True, blank=True)
    temperatura_actual = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    condicion_text = models.CharField(max_length=100,null=True, blank=True)
    condicion_icono = models.URLField(null=True, blank=True)
    ultima_actualizacion_servidor =  models.DateTimeField(auto_now=True)
    ultima_actualizacion_api = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Clima actual para {self.salida_terreno} - {self.ubicacion} - {self.ultima_actualizacion_servidor}"

    class Meta:
        verbose_name = 'Clima Actual'
        verbose_name_plural = 'Climas Actuales'
        unique_together = ['salida_terreno']        



class Implemento(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    requerido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class SalidaTerrenoImplemento(models.Model):
    salida_terreno = models.ForeignKey(SalidaTerreno, on_delete=models.CASCADE, blank=True, null=True)
    implemento = models.ManyToManyField(Implemento, related_name='salida_terreno_implemento', blank=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.implemento} - Salida: {self.salida_terreno.id}"