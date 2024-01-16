from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalidaTerrenoForm
from .models import SalidaTerreno
from core.decorators import Coordinador_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required
@Coordinador_required
def home_coordinador(request):
    return render(request, 'db_coordinador/db_home_c.html')


@login_required
@Coordinador_required
def gest_users(request):
    return render(request, 'db_coordinador/db_coordinador_gest_users.html')


@login_required
@Coordinador_required
def crear_salida(request):
    mensaje = ""  # Inicializa la variable con un valor predeterminado
    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Salida creada correctamente!")
            return redirect(to="listar_salida")
    else:
        form = SalidaTerrenoForm()
    return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form, 'mensaje': mensaje})


@login_required
@Coordinador_required
def listar_salida(request):
    salidas = SalidaTerreno.objects.all()

    data = {
        'salidas': salidas
    }

    return render(request, 'db_coordinador/db_listar_salida.html', data)


@login_required
@Coordinador_required
def editar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)

    data = {
        'form': SalidaTerrenoForm(instance=salida)
    }

   

    if request.method == 'POST':
        formulario = SalidaTerrenoForm(data=request.POST, instance=salida, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_salida")
        data["form"] = formulario

    return render(request, 'db_coordinador/db_editar_salida.html', data)


@login_required
@Coordinador_required
def eliminar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)
    salida.delete()
    messages.success(request, "Eliminado correctamente!")
    return redirect(to="listar_salida")


@login_required
@Coordinador_required
def listar_alumnos_sl(request):
    return render(request, 'db_coordinador/db_coordinador_listar_alumnos_sl.html')
