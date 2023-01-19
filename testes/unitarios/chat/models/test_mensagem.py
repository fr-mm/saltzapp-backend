from django.test import TestCase

from chat.models import Usuario, Mensagem, UltimaMensagem
from testes.fabricas import FabricaTesteUsuario


class TestMensagem(TestCase):
    def setUp(self) -> None:
        self.usuario_origem: Usuario = FabricaTesteUsuario.create()
        self.usuario_destino: Usuario = FabricaTesteUsuario.create()

    def test_criar_QUANDO_chamado_ENTAO_atualiza_ultima_mensagem(self) -> None:
        Mensagem.criar(
            origem_id=self.usuario_origem.id,
            destino_id=self.usuario_destino.id,
            texto='foo'
        )

        self.assertEqual(len(UltimaMensagem.objects.all()), 1)
