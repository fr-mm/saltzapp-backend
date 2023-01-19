from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from chat.models import Usuario, Mensagem, UltimaMensagem
from testes.fabricas import FabricaTesteUsuario, FabricaTesteMensagem


class TestRotaUltimasMensagens(TestCase):
    def setUp(self) -> None:
        self.usuario: Usuario = FabricaTesteUsuario.create()

    def get(self) -> Response:
        return self.client.get(
            path=reverse('ultimas_mensagens', kwargs={'usuario_id': str(self.usuario.id)}),
            content_type='application/json'
        )

    def test_get_QUANDO_usuario_existe_ENTAO_retorna_status_200(self) -> None:
        response = self.get()

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_ultimas_mensagens_existem_ENTAO_retorna_ultimas_mensagens_esperadas(self) -> None:
        outro_usuario_1: Usuario = FabricaTesteUsuario.create()
        outro_usuario_2: Usuario = FabricaTesteUsuario.create()
        outro_usuario_3: Usuario = FabricaTesteUsuario.create()
        mensagem_usuario_1: Mensagem = FabricaTesteMensagem.create(
            origem=self.usuario,
            destino=outro_usuario_1,
            texto='mensagem de usuario para outro usuario 1'
        )
        mensagem_usuario_2: Mensagem = FabricaTesteMensagem.create(
            origem=outro_usuario_2,
            destino=self.usuario,
            texto='mensagem de outro usuario 2 para usuario'
        )
        mensagem_usuarios_2_3: Mensagem = FabricaTesteMensagem.create(
            origem=outro_usuario_2,
            destino=outro_usuario_3,
            texto='mensagem de outro usuario 2 para outro usuario 3'
        )
        usuario_e_outro_1 = sorted([self.usuario, outro_usuario_1], key=lambda usuario: usuario.id)
        usuario_e_outro_2 = sorted([self.usuario, outro_usuario_2], key=lambda usuario: usuario.id)
        usuarios_2_3 = sorted([outro_usuario_2, outro_usuario_3], key=lambda usuario: usuario.id)
        ultima_mensagem_usuario_1 = UltimaMensagem(
            usuario_1=usuario_e_outro_1[0],
            usuario_2=usuario_e_outro_1[1],
            mensagem=mensagem_usuario_1
        )
        ultima_mensagem_usuario_2 = UltimaMensagem(
            usuario_1=usuario_e_outro_2[0],
            usuario_2=usuario_e_outro_2[1],
            mensagem=mensagem_usuario_2
        )
        ultima_mensagem_usuarios_2_3 = UltimaMensagem(
            usuario_1=usuarios_2_3[0],
            usuario_2=usuarios_2_3[1],
            mensagem=mensagem_usuarios_2_3
        )
        ultima_mensagem_usuario_1.save()
        ultima_mensagem_usuario_2.save()
        ultima_mensagem_usuarios_2_3.save()

        response = self.get()

        ids_na_response = [otd['id_outro_usuario'] for otd in response.data]
        ids_esperados = [str(usuario.id) for usuario in [outro_usuario_2, outro_usuario_1]]
        self.assertEqual(ids_na_response, ids_esperados)
