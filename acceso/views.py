
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from requests import request 
from .forms import  CustomUserCreationForm
from django.shortcuts import render, redirect


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
            return HttpResponseRedirect('')

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
