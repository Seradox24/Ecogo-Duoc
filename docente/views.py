from pyexpat.errors import messages
from django.shortcuts import redirect, render
from core.models import Asignatura
from django.shortcuts import render
from core.decorators import Docente_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django import forms
from django.utils import timezone

def home_docente(request):
    return render(request, 'db_docente/db_home_d.html')

def ji_docente(request):
    return render(request, 'db_docente/db_docente_asis.html')


def msalida_docente(request):
    return render(request, 'db_docente/db_docente_mysali.html')


def crear_salida(request):
    return render(request, 'db_docente/db_docente_crear_sl.html')


def gest_asig(request):
    return render(request, 'db_docente/db_docente_gest_asig.html')


def agreg_asig(request):
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')[:100]
        sigla = request.POST.get('sigla')[:10]
        nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
        nueva_asignatura.save()
        return redirect('gest_asig')

    return render(request, 'db_docente/db_docente_agreg_asig.html', {'mensaje': mensaje})

def gest_asig(request):
    asignaturas = Asignatura.objects.all().order_by('-id')
    asignaturas = reversed(asignaturas) 
    return render(request, 'db_docente/db_docente_gest_asig.html', {'asignaturas': asignaturas})
    

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'sigla', 'docentes', 'secciones',]


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


def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('gest_asig') 
    return render(request, 'db_docente/db_docente_gest_asig.html', {'asignatura': asignatura})
