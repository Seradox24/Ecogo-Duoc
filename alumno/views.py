from django.shortcuts import render



def home_alumno(request):
    return render(request, 'db_alumno/db_home.html',)

# Create your views here.
