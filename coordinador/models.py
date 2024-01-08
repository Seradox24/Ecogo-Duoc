from django.db import models

# Create your models here.

class SalidaTerreno(models.Model):
    situacion = models.CharField()
    numero_cuenta = models.IntegerField()
    semestre = models.CharField()
    anio = models.IntegerField()
    semana = models.IntegerField()
    actividad = models.CharField()
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    dias = models.IntegerField()
    noches = models.IntegerField()
    dias_actividad = models.IntegerField()
    lugar_ejecucion = models.CharField()
    asignatura = models.CharField()
    exp_aprendizaje = models.CharField()
    num_alumnos = models.IntegerField()
    seccion_docente = models.CharField()
    docente_titular = models.CharField()
    docentes_apoyo = models.TextField()
    num_salida = models.IntegerField()
    asig_comp_terreno = models.CharField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Salida Terreno - {self.id}"

