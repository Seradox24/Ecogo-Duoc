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