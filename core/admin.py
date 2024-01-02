from django.contrib import admin
from .models import Log, Perfiles, Genero, Pais, Region, Comuna, Seccion, Asignatura, UsersMetadata

# Define el modelo del administrador para cada modelo
class LogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'level', 'message']
    search_fields = ['timestamp', 'level', 'message']

class PerfilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id', 'region', 'nombre']
    search_fields = ['region__nombre', 'nombre']

class SeccionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'sigla']
    search_fields = ['nombre', 'sigla']

class UsersMetadataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'estado', 'genero', 'perfil', 'pais', 'comuna']
    search_fields = ['user__first_name', 'user__last_name', 'perfil__nombre']

# Registra los modelos con sus respectivos administradores
admin.site.register(Log, LogAdmin)
admin.site.register(Perfiles, PerfilesAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(UsersMetadata, UsersMetadataAdmin)

admin.site.site_header = 'Administración Eco-Go'
admin.site.index_title = 'Administración Eco-Go'
admin.site.site_title = 'Administración Eco-Go'