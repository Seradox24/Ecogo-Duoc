from django.shortcuts import render
from .forms import SalidaTerrenoForm


# Create your views here.


def home_coordinador(request):
    return render(request, 'db_coordinador/db_home_c.html')


def gest_users(request):
    return render(request, 'db_coordinador/db_coordinador_gest_users.html')


def crear_salida(request):
    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('db_coordinador/db_home_c.html')
    else:
        form = SalidaTerrenoForm()
    return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form})

