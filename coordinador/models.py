# from django.core.validators import MaxValueValidator
# from django.db import models
# from core.models import *

# # Create your models here.

# class SalidaTerreno(models.Model):
#     situacion = models.CharField()
#     numero_cuenta = models.IntegerField()
#     semestre = models.CharField()
#     anio = models.PositiveIntegerField(validators=[MaxValueValidator(3000)])
#     semana = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
#     actividad = models.CharField()
#     fecha_ingreso = models.DateField()
#     fecha_termino = models.DateField()
#     dias = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
#     noches = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
#     dias_actividad = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
#     lugar_ejecucion = models.CharField(max_length=60)
#     asignatura = models.CharField()
#     exp_aprendizaje = models.CharField()
#     num_alumnos = models.PositiveIntegerField(validators=[MaxValueValidator(150)])
#     seccion_docente = models.CharField()
#     docente_titular = models.CharField()
#     docentes_apoyo = models.TextField(max_length=100)
#     num_salida = models.IntegerField(validators=[MaxValueValidator(999)])
#     asig_comp_terreno = models.CharField()
#     observaciones = models.TextField()

#     def __str__(self):
#         return f"Salida Terreno - {self.id}"


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
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='salidas_terreno_asignatura', blank=True, null=True)
    exp_aprendizaje = models.ForeignKey(ExpAprendizaje, on_delete=models.CASCADE, blank=True, null=True)
    num_alumnos = models.PositiveIntegerField(validators=[MaxValueValidator(150)], blank=True, null=True)
    seccion =  models.ManyToManyField(Seccion, related_name='salidas_terreno',blank=True,)
    docente_titular = models.ForeignKey(UsersMetadata, on_delete=models.CASCADE, related_name='salidas_terreno_titular',  blank=True, null=True)
    docentes_apoyo = models.ManyToManyField(UsersMetadata, related_name='salidas_terreno_apoyo',  blank=True,)
    num_salida = models.IntegerField(validators=[MaxValueValidator(999)])
    asig_comp_terreno = models.ManyToManyField(Asignatura, related_name='salidas_terreno_asig_comp_terreno', blank=True)
    observaciones = models.TextField()

    def __str__(self):
        return f"Salida Terreno - {self.actividad} - {self.id}"

    class Meta:
        verbose_name = 'Salida Terreno'
        verbose_name_plural = 'Salidas Terreno'
