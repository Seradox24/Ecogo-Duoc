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


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'genero'
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Pais(models.Model):
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


class Seccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    alumnos = models.ManyToManyField('UsersMetadata', related_name='secciones', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'secciones'
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'


class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    docentes = models.ManyToManyField('UsersMetadata', related_name='asignaturas', blank=True)
    secciones = models.ManyToManyField(Seccion, related_name='asignaturas', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'asignaturas'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

class UsersMetadata(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usersmetadata')
    estado = models.BooleanField(default=True)
    genero = models.ForeignKey(Genero, models.DO_NOTHING)
    perfil = models.ForeignKey(Perfiles, models.DO_NOTHING)
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, default=1)
    slug = models.CharField(max_length=100, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
    


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        db_table = 'users_metadata'
        verbose_name = 'User metadata'
        verbose_name_plural = 'User metadata'







