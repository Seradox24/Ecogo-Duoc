from django.shortcuts import render
from core.models import UsersMetadata, Perfiles
from core.decorators import Alumno_required
from django.contrib.auth.decorators import login_required
import json


def home_alumno(request):
    paginas = "home_alumno"
    user = request.user
    
    user_metadata = UsersMetadata.objects.get(user=user)
    return render(request, 'db_alumno/db_home.html')


def ji_alumno(request):
    return render(request, 'db_alumno/db_alumno_asis.html')


def msalida_alumno(request):
    return render(request, 'db_alumno/db_alumno_mysali.html')


def aperfil(request):
    return render(request, 'db_alumno/db_alumno_perfil.html')

# Create your views here.
