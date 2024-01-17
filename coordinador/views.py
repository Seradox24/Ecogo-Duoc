from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SalidaTerrenoForm, UsersMetadataForm
from .models import SalidaTerreno
from core.decorators import Coordinador_required
from django.contrib.auth.decorators import login_required
from core.models import UsersMetadata
from django.contrib.auth.decorators import login_required
from .forms import UserCreationWithMetadataForm, UsersMetadataForm


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
    mensaje = ""
    if request.method == 'POST':
        form = SalidaTerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'db_coordinador/db_coordinador_crear_sl.html', {'form': form, 'success': True})
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
            return redirect(to="listar_salida")
        data["form"] = formulario

    return render(request, 'db_coordinador/db_editar_salida.html', data)


@login_required
@Coordinador_required
def eliminar_salida(request, id):
    salida = get_object_or_404(SalidaTerreno, id=id)
    salida.delete()
    return redirect(to="listar_salida")





@login_required
@Coordinador_required
def gest_usuarios(request):
    if request.method == 'POST':
        form = UsersMetadataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista')
    else:
        form = UsersMetadataForm()

    return render(request, 'db_coordinador/db_gest_usuarios.html', {'form': form})


def agreg_usuarios(request):
    if request.method == 'POST':
        user_form = UserCreationWithMetadataForm(request.POST)
        metadata_form = UsersMetadataForm(request.POST)

        if user_form.is_valid() and metadata_form.is_valid():
            user = user_form.save()
            metadata = metadata_form.save(commit=False)
            metadata.user = user
            metadata.username_field = user.username
            metadata.save()
            return redirect('gest_usuarios') 
    else:
        user_form = UserCreationWithMetadataForm()
        metadata_form = UsersMetadataForm()

    return render(request, 'db_coordinador/db_agreg_usuarios.html', {'user_form': user_form, 'metadata_form': metadata_form})


def gest_usuarios(request):
    usuarios = UsersMetadata.objects.all()
    return render(request, 'db_coordinador/db_gest_usuarios.html', {'usuarios': usuarios})


def edit_usuarios(request, id):
    usuario = get_object_or_404(UsersMetadata, id=id)

    if request.method == 'POST':
        user_form = UserCreationWithMetadataForm(request.POST, instance=usuario.user)
        metadata_form = UsersMetadataForm(request.POST, instance=usuario)

        if user_form.is_valid() and metadata_form.is_valid():
            
            if user_form.cleaned_data['username'] != usuario.user.username or user_form.cleaned_data['email'] != usuario.user.email:
                user_form.save()

            metadata_form.save()

            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('lista_usuarios')

    else:
        user_form = UserCreationWithMetadataForm(instance=usuario.user)
        metadata_form = UsersMetadataForm(instance=usuario)

    return render(request, 'db_coordinador/db_edit_usuarios.html', {'user_form': user_form, 'metadata_form': metadata_form, 'usuario': usuario})


def eliminar_usuarios(request):
    return render(request, 'db_coordinador/db_gest_usuarios.html')

