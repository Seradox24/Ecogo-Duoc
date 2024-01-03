from django.urls import path, include
from core import views
from .views import *

urlpatterns = [
	path('home/', home_coordinador, name="home_coordinador"),
    path('gest-users/', gest_users, name="gest_users"),
	path('crear-salida/', crear_salida,  name="crear_salida"),
]