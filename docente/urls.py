from django.urls import path, include
from .views import *

urlpatterns = [
	path('home/', home_docente, name="home_docente"),
	path('j-inasistencia/', ji_docente, name="ji_docente"),
	path('mis-salida/', msalida_docente, name="msalida_docente"),
    path('gest-users/', gest_users, name="gest_users"),
	path('crear-salida/', crear_salida,  name="crear_salida")
]