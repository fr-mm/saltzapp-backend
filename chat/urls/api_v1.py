from django.urls import path

from chat.views import UsuariosView

urlpatterns = [
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
]
