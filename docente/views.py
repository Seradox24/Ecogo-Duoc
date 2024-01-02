from django.shortcuts import render

# Create your views here.
def home_docente(request):
    return render(request, 'db_docente/db_home_d.html')


def ji_docente(request):
    return render(request, 'db_docente/db_docente_asis.html')

def msalida_docente(request):
    return render(request, 'db_docente/db_docente_mysali.html')

def gest_users(request):
    return render(request, 'db_docente/db_docente_gest_users.html')

def crear_salida(request):
    return render(request, 'db_docente/db_docente_crear_sl.html')