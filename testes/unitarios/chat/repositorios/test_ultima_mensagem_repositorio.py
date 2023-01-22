from django.test import TestCase

from chat.models import UltimaMensagem, Mensagem
from chat.repositorios import UltimaMensagemRepositorio
from testes.fabricas import FabricaTesteUsuario, FabricaTesteMensagem


class TestUltimaMensagemRepositorio(TestCase):
    def test_trazer_todas_QUANDO_existem_ENTAO_traz(self) -> None:
        usuarios = [FabricaTesteUsuario.create() for _ in range(3)]
        mensagens = [
            FabricaTesteMensagem.create(origem=usuarios[0], destino=usuarios[1]),
            FabricaTesteMensagem.create(origem=usuarios[1], destino=usuarios[2])
        ]
        for mensagem in mensagens:
            UltimaMensagem.objects.create(
                usuario_1=mensagem.origem,
                usuario_2=mensagem.destino,
                mensagem=mensagem
            )

        ultimas_mensagens = UltimaMensagemRepositorio.trazer_todas(usuarios[1].id)

        self.assertEqual(len(ultimas_mensagens), 2)

    def test_trazer_especifica_QUANDO_existe_ENTAO_traz(self) -> None:
        mensagem: Mensagem = FabricaTesteMensagem.create()
        ultima_mensagem = UltimaMensagem.objects.create(
            usuario_1=mensagem.origem,
            usuario_2=mensagem.destino,
            mensagem=mensagem
        )

        resultado = UltimaMensagemRepositorio.trazer_especifica(mensagem.origem.id, mensagem.destino.id)

        self.assertEqual(resultado, ultima_mensagem)
