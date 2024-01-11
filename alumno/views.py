from django.shortcuts import render
from core.models import UsersMetadata, Perfiles
from core.decorators import Alumno_required
from django.contrib.auth.decorators import login_required


@login_required
@Alumno_required
def home_alumno(request):
    paginas = "home_alumno"
    user = request.user
    
    user_metadata = UsersMetadata.objects.get(user=user)
    return render(request, 'db_alumno/db_home.html')

@login_required
@Alumno_required
def ji_alumno(request):
    return render(request, 'db_alumno/db_alumno_asis.html')

@login_required
@Alumno_required
def msalida_alumno(request):
    return render(request, 'db_alumno/db_alumno_mysali.html')

@login_required
def aperfil(request):
    return render(request, 'db_alumno/db_alumno_perfil.html')

# Create your views here.
