from django.urls import include, path
from .views import *
from .views import registro
from django import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', acceso_login, name="acceso_login"),
	path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('allauth.urls')),
    path('registro/', registro, name='registro'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]