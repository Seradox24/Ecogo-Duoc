from django.shortcuts import render
from .forms import SalidaTerrenoForm


# Create your views here.


def home_coordinador(request):
    return render(request, 'db_coordinador/db_home_c.html')


def gest_users(request):
    return render(request, 'db_coordinador/db_coordinador_gest_users.html')


def crear_salida(request):
    mensaje = ""  # Inicializa la variable con un valor predeterminado
    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form, 'success': True})
    else:
        form = SalidaTerrenoForm()
    return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form, 'mensaje': mensaje})


