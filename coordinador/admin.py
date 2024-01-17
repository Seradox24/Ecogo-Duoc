# En el archivo admin.py de tu aplicación (por ejemplo, 'core/admin.py')

from django.contrib import admin
from .models import Situacion, DiaSemana, Actividad, ExpAprendizaje, SalidaTerreno

@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    list_display = ['estado']

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(ExpAprendizaje)
class ExpAprendizajeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']


