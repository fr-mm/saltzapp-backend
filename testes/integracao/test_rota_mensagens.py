import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from chat.models import Mensagem, Usuario, UltimaMensagem
from testes.fabricas import FabricaTesteUsuario, FabricaTesteMensagem


class TestRotaMensagens(TestCase):
    def setUp(self) -> None:
        self.usuario_origem: Usuario = FabricaTesteUsuario.create()
        self.usuario_destino: Usuario = FabricaTesteUsuario.create()
        usuarios = sorted([self.usuario_origem, self.usuario_destino], key=lambda usuario: usuario.id)
        self.ultima_mensagem = UltimaMensagem(
            usuario_1=usuarios[0],
            usuario_2=usuarios[1],
            mensagem=FabricaTesteMensagem.create(
                origem=self.usuario_origem,
                destino=self.usuario_destino
            )
        )
        self.ultima_mensagem.save()
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

        Mensagem.objects.get(texto=self.payload['texto'])

    def test_post_QUANDO_ultima_mensagem_existe_ENTAO_atualiza_ultima_mensagem(self) -> None:
        self.post(self.payload)

        UltimaMensagem.objects.get(mensagem__texto=self.payload['texto'])
