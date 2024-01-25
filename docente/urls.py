from django.urls import path, include
from core import views
from docente import views
from .views import *

urlpatterns = [
	path('home/', home_docente, name="home_docente"),
	path('j-inasistencia/', ji_docente, name="ji_docente"),
	path('mis-salida/', msalida_docente, name="msalida_docente"),
    path('gest-asig-docente/', gest_asig_docente, name='gest_asig_docente'),
    path('docente-listar-salida/', docente_listar_salida, name="docente_listar_salida"),

]