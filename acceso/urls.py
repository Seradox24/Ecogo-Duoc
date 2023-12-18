from django.urls import path, include
from .views import *



urlpatterns = [
	path('', acceso_login, name="acceso_login"),
	path('accounts/', include('django.contrib.auth.urls')),     
	path('accounts/', include('allauth.urls')),

]