from django.urls import include, path
from .views import *
from acceso.views import register
from django import views

urlpatterns = [
	path('', acceso_login, name="acceso_login"),
	path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('registro/', register, name="registro"),
]