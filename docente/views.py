from pyexpat.errors import messages
from django.shortcuts import redirect, render
from core.models import Asignatura
# Create your views here.
def home_docente(request):
    return render(request, 'db_docente/db_home_d.html')

def ji_docente(request):
    return render(request, 'db_docente/db_docente_asis.html')

def msalida_docente(request):
    return render(request, 'db_docente/db_docente_mysali.html')

def gest_users(request):
    return render(request, 'db_docente/db_docente_gest_users.html')

def gest_users(request):
    return render(request, 'db_docente/db_docente_gest_users.html')

def agreg_asig(request):
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')[:100]
        sigla = request.POST.get('sigla')[:10]
        # Crear una nueva instancia de Asignatura y guardarla en la base de datos
        nueva_asignatura = Asignatura(nombre=nombre, sigla=sigla)
        nueva_asignatura.save()

        # Definir el mensaje de éxito
        mensaje = "La asignatura se guardó correctamente."

    # Retornar solo el mensaje como respuesta
    return render(request, 'db_docente/db_docente_agreg_asig.html', {'mensaje': mensaje})

def gest_asig(request):
    asignaturas = Asignatura.objects.all()  # Obtener todas las asignaturas de la base de datos
    print(asignaturas)
    return render(request, 'docente/db_docente_gest_asig.html', {'asignaturas': asignaturas})
    

