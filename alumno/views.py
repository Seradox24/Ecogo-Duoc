from django.shortcuts import render
from core.models import UsersMetadata, Perfiles
from core.decorators import Alumno_required
from django.contrib.auth.decorators import login_required
from coordinador.models import SalidaTerreno
from django.db.models import Q
from django.utils import timezone

@login_required
@Alumno_required
def home_alumno(request):
    user = request.user
    user_metadata = UsersMetadata.objects.get(user=user)
      # Filtra las salidas de terreno según la sección, asignatura y situacion del usuario
    # Excluye las salidas de terreno cuya fecha de ingreso ya ha pasado
    salidas_terreno = SalidaTerreno.objects.filter(
        Q(seccion__alumnos=user_metadata) | Q(asignatura__docentes=user_metadata),
        situacion=6,
        fecha_ingreso__gte=timezone.now()  # Solo fechas de ingreso en el futuro
    ).order_by('fecha_ingreso')

    # Toma la primera salida de terreno después de ordenar
    primera_salida_cercana = salidas_terreno.first()
    print(primera_salida_cercana)






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
