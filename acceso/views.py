import dataclasses
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from requests import request 
from .forms import CustomUserCreationForm


@login_required
def acceso_login(request):
    return render(request, 'acceso/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirige al usuario a alguna página después del inicio de sesión exitoso
            return HttpResponseRedirect('ruta-a-tu-pagina')

    return render(request, 'acceso/login.html')

def register(request):
        data = {
            'form': CustomUserCreationForm()
        }
        return render(request, 'acceso/registro.html', data)