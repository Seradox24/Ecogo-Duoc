from django.urls import path, include
from .views import *

urlpatterns = [
	path('home/', home_alumno, name="home_alumno"),
	path('j-inasistencia/', ji_alumno, name="ji_alumno"),
	path('mis-salida/', msalida_alumno, name="msalida_alumno"),
]