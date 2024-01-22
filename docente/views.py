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
def gest_asig(request):
    return render(request, 'db_docente/db_docente_gest_asig.html')


@login_required
@Docente_required
def agreg_asig(request):
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')[:100]
        sigla = request.POST.get('sigla')[:10]
        nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
        nueva_asignatura.save()
        return redirect('gest_asig')

    return render(request, 'db_docente/db_docente_agreg_asig.html', {'mensaje': mensaje})


@login_required
@Docente_required
def gest_asig(request):
    asignaturas = Asignatura.objects.all().order_by('-id')
    asignaturas = reversed(asignaturas) 
    return render(request, 'db_docente/db_docente_gest_asig.html', {'asignaturas': asignaturas})
    



@login_required
@Docente_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('gest_asig')  
    else:
        form = AsignaturaForm(instance=asignatura)
    
    return render(request, 'db_docente/db_edit_asig.html', {'form': form, 'asignatura': asignatura})


@login_required
@Docente_required
def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('gest_asig') 
    return render(request, 'db_docente/db_docente_gest_asig.html', {'asignatura': asignatura})


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
