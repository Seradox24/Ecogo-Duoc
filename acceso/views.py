from django.shortcuts import render

# Create your views here.
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

    return render(request, 'login.html')