from django.db import models
from core.models import *
from coordinador.models import *


class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Documento_inasis(models.Model):
    nombre = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=200, default='')
    archivo = models.FileField(upload_to='documentos/')
    users_metadata = models.ForeignKey(UsersMetadata, models.SET_NULL, default=1, related_name='documentos', null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    salida_terreno = models.ForeignKey(SalidaTerreno, models.DO_NOTHING, null=True, default=None)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, null=True, default=None)

    def __str__(self):
        return self.nombre


class Bajada(models.Model):
    nombre = models.CharField(max_length=200,default='', null=True)
    descripcion = models.CharField(max_length=200,default='', null=True)
    salida_terreno = models.ForeignKey(SalidaTerreno, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class BajaEstudiante(models.Model):
    estudiante = models.ForeignKey(UsersMetadata, models.CASCADE, related_name='bajas',default='', null=True )
    bajada = models.ForeignKey(Bajada, models.CASCADE, related_name='estudiantes',default='', null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    salida_terreno = models.ForeignKey(SalidaTerreno, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'-{self.estudiante} - {self.bajada}'



# Create your models here.
