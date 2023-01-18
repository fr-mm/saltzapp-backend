from django.urls import path
from rest_framework.authtoken import views as auth_views

from chat import views

urlpatterns = [
    path('usuarios/', views.UsuariosView.as_view(), name='usuarios'),
    path('clientes/', views.ClientesView.as_view(), name='clientes'),
    path('mensagens/', views.MensagemsView.as_view(), name='mensagens'),
    path('token/', auth_views.obtain_auth_token)
]
