# En el archivo admin.py de tu aplicación (por ejemplo, 'core/admin.py')
from django.contrib import admin
from .models import Situacion, DiaSemana, Actividad, ExpAprendizaje
from .models import SalidaTerreno

class SituacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'estado']
    search_fields = ['estado']

class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class ActividadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class ExpAprendizajeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    search_fields = ['nombre']




class SalidaTerrenoAdmin(admin.ModelAdmin):
    list_display = ['id', 'situacion', 'numero_cuenta', 'semestre', 'anio', 'diasemana', 'actividad',
                    'fecha_ingreso', 'fecha_termino', 'dias', 'noches', 'dias_actividad', 'lugar_ejecucion',
                    'asignatura', 'exp_aprendizaje', 'num_alumnos', 'docente_titular', 'get_docentes_apoyo',
                    'num_salida', 'asig_comp_terreno', 'observaciones']
    search_fields = ['id', 'actividad__nombre', 'asignatura__nombre', 'docente_titular__user__first_name',
                     'docente_titular__user__last_name']

    def get_docentes_apoyo(self, obj):
        return ', '.join([docente.user.get_full_name() for docente in obj.docentes_apoyo.all()])

    get_docentes_apoyo.short_description = 'Docentes de Apoyo'

# Registra el modelo con su respectivo administrador
admin.site.register(SalidaTerreno, SalidaTerrenoAdmin)
# Registra los modelos con sus respectivos administradores
admin.site.register(Situacion, SituacionAdmin)
admin.site.register(DiaSemana, DiaSemanaAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(ExpAprendizaje, ExpAprendizajeAdmin)