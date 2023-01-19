from random import shuffle

from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from chat.models import Usuario
from testes.fabricas import FabricaTesteUsuario, FabricaTesteMensagem


class TestRotaConversa(TestCase):
    def setUp(self) -> None:
        self.usuario: Usuario = FabricaTesteUsuario.create()
        self.outro_usuario: Usuario = FabricaTesteUsuario.create()

    def get(self) -> Response:
        return self.client.get(
            path=reverse(
                'ultimas_mensagens', kwargs={
                    'usuario_id': str(self.usuario.id),
                    'destino_id': str(self.outro_usuario.id)
                }
            ),
            content_type='application/json'
        )

    def test_foo(self):
        pass

    def test_get_QUANDO_usuario_existe_ENTAO_retorna_status_200(self) -> None:
        response = self.get()

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_ultimas_mensagens_existem_ENTAO_retorna_ultimas_mensagens_esperadas(self) -> None:
        mensagens_de = [
            FabricaTesteMensagem.create(
                origem=self.usuario,
                destino=self.outro_usuario
            ) for _ in range(2)
        ]
        mensagens_para = [
            FabricaTesteMensagem.create(
                origem=self.outro_usuario,
                destino=self.usuario
            ) for _ in range(2)
        ]
        mensagens = mensagens_de + mensagens_para
        shuffle(mensagens)

        response = self.get()

        datas_na_response = [otd['enviada_em'] for otd in response.data]
        datas_esperadas = sorted([mensagem.enviada_em for mensagem in mensagens], key=lambda mens: mens.enviada_em)
        self.assertEqual(datas_na_response, datas_esperadas)