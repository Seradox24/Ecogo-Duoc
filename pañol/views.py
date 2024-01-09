from django.shortcuts import render

# Create your views here.



def home_pañol(request):
    return render(request, 'db_pañol/home_pañol.html')