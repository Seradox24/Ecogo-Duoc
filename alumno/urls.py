from django.urls import path, include
from .views import *

urlpatterns = [
	path('home/', home_alumno, name="home_alumno"),
	path('j-inasistencia/', ji_alumno, name="ji_alumno"),
	path('mis-salida/', msalida_alumno, name="msalida_alumno"),
    path('perfil/', aperfil, name="aperfil"),
    path('subir_documento/<int:salida_terreno_id>/', subir_documento, name='subir_documento'),
    path('evaluar_documento/<int:documento_id>/', evaluar_documento, name='evaluar_documento'),
]