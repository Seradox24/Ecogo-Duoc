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

@login_required
@Docente_required
def home_docente(request):
    return render(request, 'db_docente/db_home_d.html')


@login_required
@Docente_required
def ji_docente(request):
    return render(request, 'db_docente/db_docente_asis.html')


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

    salidas = SalidaTerreno.objects.all()
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
