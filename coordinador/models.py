from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class SalidaTerreno(models.Model):
    situacion = models.CharField()
    numero_cuenta = models.IntegerField()
    semestre = models.CharField()
    anio = models.PositiveIntegerField(validators=[MaxValueValidator(3000)])
    semana = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    actividad = models.CharField()
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    dias = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    noches = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    dias_actividad = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    lugar_ejecucion = models.CharField(max_length=60)
    asignatura = models.CharField()
    exp_aprendizaje = models.CharField()
    num_alumnos = models.PositiveIntegerField(validators=[MaxValueValidator(150)])
    seccion_docente = models.CharField()
    docente_titular = models.CharField()
    docentes_apoyo = models.TextField(max_length=100)
    num_salida = models.IntegerField(validators=[MaxValueValidator(999)])
    asig_comp_terreno = models.CharField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Salida Terreno - {self.id}"

