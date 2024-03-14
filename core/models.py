from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from datetime import datetime, date
from django.utils.text import slugify



class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=60)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.timestamp} {self.level} {self.message}"



class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'perfiles'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'genero'
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Nacionalidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Países'

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'region'
        verbose_name = 'Región'
        verbose_name_plural = 'Región'


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, default=1)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'comuna'
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'




class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    #docentes = models.ManyToManyField('UsersMetadata', related_name='asignaturas', blank=True)
    #secciones = models.ManyToManyField(Seccion, related_name='asignaturas', blank=True)

    def __str__(self):
        return f"{self.nombre} - Sigla {self.sigla} "

    class Meta:
        db_table = 'asignaturas'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    





class ContactoEmergencia(models.Model):
    nombre1 = models.CharField(max_length=100, blank=True, null=True)
    relacion1 = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=100, blank=True, null=True)
    nombre2 = models.CharField(max_length=100, blank=True, null=True)
    relacion2 = models.CharField(max_length=100, blank=True, null=True)
    telefono2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre1} {self.relacion1} {self.telefono1}'

class UsersMetadata(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usersmetadata')
    estado = models.BooleanField(default=True)
    sexo = models.ForeignKey(Sexo, models.DO_NOTHING)
    perfil = models.ForeignKey(Perfiles, models.DO_NOTHING)
    nacionalidad= models.ForeignKey(Nacionalidad, models.DO_NOTHING, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, default=1, blank=True, null=True)
    correoduoc = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    sede = models.CharField(max_length=100, blank=True, null=True)
    nom_carrera = models.CharField(max_length=100, blank=True, null=True)
    modalidad = models.CharField(max_length=100, blank=True, null=True)
    jornada = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=100, blank=True, null=True, unique=True)
    nombres = models.CharField(max_length=100, blank=True, null=True)
    ap_paterno = models.CharField(max_length=100, blank=True, null=True)
    ap_materno = models.CharField(max_length=100, blank=True, null=True)
    fnacimiento = models.DateField(blank=True, null=True)
    estado_civil = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=100, blank=True, null=True)
    contacto_emergencia = models.ForeignKey(ContactoEmergencia, on_delete=models.CASCADE, blank=True, null=True)
    asignaturas_inscritas = models.ManyToManyField(Asignatura, related_name='alumnos_inscritos', blank=True)

    def __str__(self):
        return f'{self.nombres} {self.ap_paterno} {self.ap_materno} '

    class Meta:
        verbose_name = 'User Metadata'
        verbose_name_plural = 'Users Metadata'
 

class NombreSeccion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.nombre


class Seccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.ForeignKey(NombreSeccion, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, default=None)
    usuarios = models.ManyToManyField(UsersMetadata, related_name='secciones', blank=True)
    

    def __str__(self):
        return f"{self.asignatura.nombre} - Sección {self.nombre}"

    class Meta:
        db_table = 'secciones'
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'