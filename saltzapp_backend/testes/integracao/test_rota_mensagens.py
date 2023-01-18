import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from chat.models import Mensagem, Usuario
from saltzapp_backend.testes.fabricas import FabricaTesteUsuario


class TestRotaMensagens(TestCase):
    def setUp(self) -> None:
        self.usuario_origem: Usuario = FabricaTesteUsuario.create()
        self.usuario_destino: Usuario = FabricaTesteUsuario.create()
        self.payload = {
            'origem_id': str(self.usuario_origem.id),
            'destino_id': str(self.usuario_destino.id),
            'texto': 'corpo da mensagem'
        }

    def post(self, payload: {}) -> Response:
        return self.client.post(
            path=reverse('mensagens'),
            data=json.dumps(payload),
            content_type='application/json'
        )

    def test_post_QUANDO_payload_valido_ENTAO_retorna_status_201(self) -> None:
        response = self.post(self.payload)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_payload_invalido_ENTAO_retorna_status_400(self) -> None:
        response = self.post({})

        self.assertEqual(response.status_code, 400)

    def test_post_QUANDO_payload_valido_ENTAO_cria_mensagem(self) -> None:
        self.post(self.payload)

        Mensagem.objects.get(origem_id=self.usuario_origem.id)
