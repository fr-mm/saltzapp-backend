from django.urls import path
from rest_framework.authtoken import views

from chat.views import UsuariosView

urlpatterns = [
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('token/', views.obtain_auth_token)
]
