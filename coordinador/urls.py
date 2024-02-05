from django.urls import path, include
from core import views
from core import views
from coordinador import views
from .views import *


urlpatterns = [
	  path('home/', home_coordinador, name="home_coordinador"),
    path('gest-users/', gest_users, name="gest_users"),
    path('crear-salida/', crear_salida,  name="crear_salida"),
    path('listar-salida/', listar_salida, name="listar_salida"),
    path('editar-salida/<int:id>/', editar_salida, name="editar_salida"),
    path('eliminar-salida/<int:id>/', eliminar_salida, name="eliminar_salida"),
    path('editar-salida/<id>/', editar_salida, name="editar_salida"),
    path('eliminar-salida/<id>/', eliminar_salida, name="eliminar_salida"),
    path('gest-usuarios/', gest_usuarios, name='gest-usuarios'),
    path('agreg-usuarios/', agreg_usuarios, name='agreg-usuarios'),
    path('edit-usuarios/<int:id>/', edit_usuarios, name='edit-usuarios'),
    path('eliminar-usuarios/<int:id>/', eliminar_usuarios, name='eliminar-usuarios'),
	  path('listar-alumnos-sl/', listar_alumnos_sl, name="listar_alumnos_sl"),
	  path('carga-masiva-alumno/', carga_masiva_alumno, name="carga_masiva_alumno"),
    path('cargar-datos/', cargar_datos, name="cargar_datos"),
    path('eliminar-usuarios-mv/', eliminar_usuarios_mv, name="eliminar_usuarios_mv"),
	  path('agreg-asig/', agreg_asig, name="agreg_asig"),
    path('gest-asig/', gest_asig, name='gest_asig'),
    path('editar_asignatura/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('eliminar_asignatura/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('semaforo-salida/<id>/', semaforo_salida, name="semaforo_salida"),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
] 