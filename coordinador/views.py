from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalidaTerrenoForm
from .models import SalidaTerreno


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


def listar_salida(request):
    salidas = SalidaTerreno.objects.all()

    data = {
        'salidas': salidas
    }

    return render(request, 'db_coordinador/db_listar_salida.html', data)


def editar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)

    data = {
        'form': SalidaTerrenoForm(instance=salida)
    }

    if request.method == 'POST':
        formulario = SalidaTerrenoForm(data=request.POST, instance=salida, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_salida")
        data["form"] = formulario

    return render(request, 'db_coordinador/db_editar_salida.html', data)


def eliminar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)
    salida.delete()
    return redirect(to="listar_salida")
