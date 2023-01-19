from django.urls import path
from rest_framework.authtoken import views as auth_views

from chat import views

urlpatterns = [
    path('clientes/', views.ClientesView.as_view(), name='clientes'),
    path('mensagens/', views.MensagensView.as_view(), name='mensagens'),
    path('usuarios/', views.UsuariosView.as_view(), name='usuarios'),
    path('usuarios/<uuid:usuario_id>', views.UltimasMensagemsView.as_view(), name='ultimas_mensagens'),
    path('usuarios/<uuid:usuario_id>/<uuid:destino_id>', views.ConversaView.as_view(), name='conversa'),
    path('token/', auth_views.obtain_auth_token)
]
