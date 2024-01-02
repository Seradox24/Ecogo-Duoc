from django.urls import path, include
from core import views
from .views import *

urlpatterns = [
	path('home/', home_docente, name="home_docente"),
	path('j-inasistencia/', ji_docente, name="ji_docente"),
	path('mis-salida/', msalida_docente, name="msalida_docente"),
    path('gest-users/', gest_users, name="gest_users"),
    path('agreg-asig/', agreg_asig, name="agreg_asig"),
    path('gest-asig/', gest_asig, name='gest_asig'),
    path('guardar_asignatura/', views.guardar_asignatura, name='guardar_asignatura'),
    
]