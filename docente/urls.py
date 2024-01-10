from django.urls import path, include
from core import views
from docente import views
from .views import *

urlpatterns = [
	path('home/', home_docente, name="home_docente"),
	path('j-inasistencia/', ji_docente, name="ji_docente"),
	path('mis-salida/', msalida_docente, name="msalida_docente"),
	path('crear-salida/', crear_salida,  name="crear_salida"),
    path('agreg-asig/', agreg_asig, name="agreg_asig"),
    path('gest-asig/', gest_asig, name='gest_asig'),
    path('editar_asignatura/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('eliminar_asignatura/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    

]