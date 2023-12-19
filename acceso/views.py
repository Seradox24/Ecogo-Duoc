from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from requests import request 
from .forms import  CustomUserCreationForm
from django.shortcuts import render, redirect


def acceso_login(request):
    return render(request, 'acceso/login.html')