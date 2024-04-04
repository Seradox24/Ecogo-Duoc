from django.urls import path, include
from core import views
from core import views
from coordinador import views
from .views import *


urlpatterns = [
	path('home/', home_coordinador, name="home_coordinador"),  
    path('crear-salida/', crear_salida,  name="crear_salida"),
    path('listar-salida/', listar_salida, name="listar_salida"),
    path('editar-salida/<int:id>/', editar_salida, name="editar_salida"),
    path('eliminar-salida/<int:id>/', eliminar_salida, name="eliminar_salida"),
    #path('editar-salida/<id>/', editar_salida, name="editar_salida"),
    path('eliminar-salida/<id>/', eliminar_salida, name="eliminar_salida"),
    path('gest-usuarios/', gest_usuarios, name='gest-usuarios'),
    path('agreg-usuarios/', agreg_usuarios, name='agreg-usuarios'),
    path('edit-usuarios/<int:id>/', edit_usuarios, name='edit-usuarios'),
    path('eliminar-usuarios/<int:id>/', eliminar_usuarios, name='eliminar-usuarios'),
	path('carga-masiva-alumno/', carga_masiva_alumno, name="carga_masiva_alumno"),
    path('cargar-datos/', cargar_datos, name="cargar_datos"),
    path('eliminar-usuarios-mv/', eliminar_usuarios_mv, name="eliminar_usuarios_mv"),
	path('agreg-asig/', agreg_asig, name="agreg_asig"),
    path('gest-asig/', gest_asig, name='gest_asig'),
    path('editar_asignatura/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('eliminar_asignatura/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('semaforo-salida/<id>/', semaforo_salida, name="semaforo_salida"),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('ver-perfil-usuario/<int:usuario_id>/', ver_perfil_usuario, name='ver_perfil_usuario'),
    path('manual-coordinador/', manual_coordinador, name="manual_coordinador"),
    path('generate-pdf/<int:salida_id>/', views.generar_pdf, name='generar_pdf'),
    path('salida_terreno/<int:salida_terreno_id>/implementos/', lista_implementos_salida, name='lista_implementos_salida'),
    path('obtener_secciones/', obtener_secciones, name='obtener_secciones'),
    path('editar_seccion/<int:seccion_id>/', views.editar_seccion, name='editar_seccion'),
    path('obtener_asig_base/', obtener_asig_base, name='obtener_asig_base'),
    path('enviar-correos/<int:salida_id>/', views.enviar_correos, name='enviar_correos'),
    path('eliminar-documento/<int:documento_id>/', eliminar_documento, name='eliminar_documento'),
    path('salidas/<int:salida_id>/agregar-documentos/', agregar_documentos_salida, name='agregar_documentos_salida'),
    path('salidas/<int:salida_id>/eliminar-documento/<int:documento_id>/', eliminar_documento_salida, name='eliminar_documento_salida'),




] 