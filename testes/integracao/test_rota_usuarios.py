import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from chat.models import Usuario, Mensagem, UltimaMensagem
from testes.fabricas import FabricaTesteUsuario


class TestRotaUsuarios(TestCase):
    def setUp(self) -> None:
        self.payload = {
            'nome': 'Nome válido',
            'senha': '123456'
        }

    def post(self, payload: {}) -> Response:
        return self.client.post(
            path=reverse('usuarios'),
            data=json.dumps(payload),
            content_type='application/json'
        )

    def test_post_QUANDO_payload_valido_ENTAO_retorna_status_201(self) -> None:
        response = self.post(self.payload)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_payload_invalido_ENTAO_retorna_status_400(self) -> None:
        response = self.post({})

        self.assertEqual(response.status_code, 400)

    def test_post_QUANDO_payload_valido_ENTAO_cria_usuario(self) -> None:
        self.post(self.payload)

        Usuario.objects.get(username=self.payload['nome'])

    def test_post_QUANDO_outro_usuario_existe_ENTAO_cria_mensagem(self) -> None:
        FabricaTesteUsuario.create()

        self.post(self.payload)

        mensagens = Mensagem.objects.all()
        self.assertEqual(len(mensagens), 1)

    def test_post_QUANDO_outro_usuario_existe_ENTAO_cria_ultima_mensagem(self) -> None:
        FabricaTesteUsuario.create()

        self.post(self.payload)

        ultimas_mensagens = UltimaMensagem.objects.all()
        self.assertEqual(len(ultimas_mensagens), 1)
