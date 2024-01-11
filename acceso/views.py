from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from requests import request 
from .forms import  CustomUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from core.models import UsersMetadata, Perfiles
from alumno.views import home_alumno
from docente.views import home_docente
from coordinador.views import home_coordinador


@user_passes_test(lambda user: not user.is_authenticated, login_url='accounts/profile/')
def acceso_login(request):
    return render(request, 'acceso/login.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('nombre_de_la_ruta')
    else:
        form = CustomUserCreationForm()
    return render(request, 'acceso/registro.html', {'form': form})



@login_required
def profile_view(request):
    # Obtener el usuario actual
    user = request.user

    # Obtener el perfil del usuario desde UsersMetadata
    try:
        user_metadata = UsersMetadata.objects.get(user=user)

        # Verificar la condición del perfil
        if user_metadata.perfil.nombre == 'Alumno':
            print('alumnito')
            return redirect('home_alumno')
        elif user_metadata.perfil.nombre == 'Docente':
            print('profe')
            return redirect('home_docente')
        elif user_metadata.perfil.nombre == 'Coordinador':
            print('profe')
            return redirect('home_coordinador')
        elif user_metadata.perfil.nombre == 'Pañol':
            print('profe')
            return redirect('home_coordinador')        
        else:
            # Puedes ajustar esta redirección según tus necesidades
            return render(request, 'db_alumno/db_home.html', {'user': user})

    except UsersMetadata.DoesNotExist:
        # Manejar el caso en el que no se encuentra el metadata del usuario
        return redirect('logout')


def acceso_error(request):
    # Aquí puedes agregar el código para obtener la información del perfil del usuario
    # Por ejemplo, puedes obtener el usuario actual con request.user
    user = request.user

    # Luego puedes renderizar una plantilla con la información del perfil
    return render(request, 'acceso/login.html', {'user': user})


def no_access(request):
    return render(request, 'acceso/no_access.html')