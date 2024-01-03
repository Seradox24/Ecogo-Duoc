from pyexpat.errors import messages
from django.shortcuts import redirect, render
from core.models import Asignatura
from django.shortcuts import render
from core.decorators import Docente_required
from django.contrib.auth.decorators import login_required

# Create your views here.
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
def gest_users(request):
    return render(request, 'db_docente/db_docente_gest_users.html')


def crear_salida(request):
    return render(request, 'db_docente/db_docente_crear_sl.html')

def gest_users(request):
    return render(request, 'db_docente/db_docente_gest_users.html')

def gest_asig(request):
    return render(request, 'db_docente/db_docente_gest_asig.html')

def agreg_asig(request):
    return render(request, 'db_docente/db_docente_agreg_asig.html')

def guardar_asignatura(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        sigla = request.POST.get('sigla')
        # Obtén otros campos del formulario si los hay

        # Crea una nueva instancia de Asignatura y guárdala en la base de datos
        nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
        nueva_asignatura.save()

        # Redirige a una página de confirmación o a donde sea necesario
        return redirect('pagina_confirmacion')

    return render(request, 'template.html')
