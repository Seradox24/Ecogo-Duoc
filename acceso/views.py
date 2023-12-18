from django.shortcuts import render

# Create your views here.
def acceso_login(request):
    return render(request, 'acceso/login.html')