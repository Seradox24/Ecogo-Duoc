from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from requests import request 
from .forms import  CustomUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: not user.is_authenticated, login_url='accounts/profile/')
def acceso_login(request):
    return render(request, 'acceso/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile_view', parametro=user.id)
        else:
            
            return redirect('acceso_login')

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
    # Aquí puedes agregar el código para obtener la información del perfil del usuario
    # Por ejemplo, puedes obtener el usuario actual con request.user
    user = request.user

    # Luego puedes renderizar una plantilla con la información del perfil
    return render(request, 'db_alumno/db_home.html', {'user': user})


def acceso_error(request):
    # Aquí puedes agregar el código para obtener la información del perfil del usuario
    # Por ejemplo, puedes obtener el usuario actual con request.user
    user = request.user

    # Luego puedes renderizar una plantilla con la información del perfil
    return render(request, 'acceso/login.html', {'user': user})


