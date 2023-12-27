from django.shortcuts import render



def home_alumno(request):
    return render(request, 'db_alumno/db_home.html')


def ji_alumno(request):
    return render(request, 'db_alumno/db_alumno_asis.html')

def msalida_alumno(request):
    return render(request, 'db_alumno/db_alumno_mysali.html')

def aperfil(request):
    return render(request, 'db_alumno/db_alumno_perfil.html')

# Create your views here.
