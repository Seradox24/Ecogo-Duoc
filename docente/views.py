from pyexpat.errors import messages
from django.shortcuts import redirect, render
from core.models import Asignatura
from django.shortcuts import render
from core.decorators import Docente_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django import forms
from django.utils import timezone
from docente.forms import AsignaturaForm
from core.models import Asignatura
from coordinador.models import SalidaTerreno
from django.core.paginator import Paginator
from django.http import Http404
from alumno.models import *

@login_required
@Docente_required
def home_docente(request):
    try:
        # Obtener el objeto Perfil con el nombre 'Alumno'
        perfil_alumno = Perfiles.objects.get(nombre='Alumno')
        # Contar todos los usuarios con el perfil de alumno
        cantidad_alumnos_g = UsersMetadata.objects.filter(perfil=perfil_alumno).count()
        # Contar todas las instancias de SalidaTerreno
        cantidad_salidas_g = SalidaTerreno.objects.count()
        # Contar todas las instancias de Asignatura
        cantidad_asignaturas_g = Asignatura.objects.count()
        # Contar todas las instancias de Seccion
        cantidad_secciones_g = Seccion.objects.count()

        # print("Cantidad total de secciones:", cantidad_secciones)
        # print("Cantidad de alumnos:", cantidad_alumnos)
        # print("Cantidad total de salidas a terreno:", cantidad_salidas)
        # print("Cantidad total de asignaturas:", cantidad_asignaturas)

        # Nuevo bloque para calcular la cantidad de secciones y alumnos por sección por asignatura
        salidas = SalidaTerreno.objects.all().order_by('fecha_ingreso')
        # Aquí se obtienen todas las salidas a terreno disponibles

        contexto = {
            'cantidad_alumnos': cantidad_alumnos_g,
            'cantidad_salidas': cantidad_salidas_g,
            'cantidad_asignaturas': cantidad_asignaturas_g,
            'cantidad_secciones': cantidad_secciones_g,
            'salidas': salidas
        }
    except Perfiles.DoesNotExist:
        # Si el perfil 'Alumno' no existe, manejar la excepción
        contexto = {'error': 'El perfil de alumno no está definido.'}
    except Exception as e:
        # Cualquier otra excepción se maneja aquí
        contexto = {'error': f'Ha ocurrido un error: {e}'}

    return render(request, 'db_coordinador/db_home_c.html', contexto)


@login_required
@Docente_required
def ji_docente(request):
    salidas = SalidaTerreno.objects.all()
    documentos_por_salida = {salida: Documento_inasis.objects.filter(salida_terreno=salida) for salida in salidas}

    return render(request, 'db_docente/db_docente_asis.html', {'documentos_por_salida': documentos_por_salida})


@login_required
@Docente_required
def msalida_docente(request):
    return render(request, 'db_docente/db_docente_mysali.html')


@login_required
@Docente_required
def gest_asig_docente(request):
    asignaturas = Asignatura.objects.all().order_by('-id')
    asignaturas = reversed(asignaturas) 
    return render(request, 'db_docente/db_docente_gest_asig.html', {'asignaturas': asignaturas})


@login_required
@Docente_required
def docente_listar_salida(request):

    salidas = SalidaTerreno.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(salidas, 5)
        salidas = paginator.page(page)
    except:
        raise Http404


    data = {
        'salidas': salidas,
        'paginator': paginator
    }

    return render(request, 'db_docente/db_docente_listar_salida.html',data)
