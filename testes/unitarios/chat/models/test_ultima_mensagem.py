from uuid import UUID

from django.test import TestCase

from chat.models import Usuario, Mensagem, UltimaMensagem
from testes.fabricas import FabricaTesteUsuario, FabricaTesteMensagem


class TestUltimaMensagem(TestCase):
    def setUp(self) -> None:
        self.usuario_origem: Usuario = FabricaTesteUsuario.create()
        self.usuario_destino: Usuario = FabricaTesteUsuario.create()
        self.mensagem: Mensagem = FabricaTesteMensagem.create(
            origem_id=self.usuario_origem.id,
            destino_id=self.usuario_destino.id
        )

    @property
    def usuarios_ids_ordenadas(self) -> [UUID]:
        return sorted([self.usuario_origem, self.usuario_destino], key=lambda usuario: usuario.id)

    def test_trazer_QUANDO_ultima_mensagem_existe_ENTAO_retorna_ultima_mensagem_com_mensagem_id_correto(self) -> None:
        ultima_mensagem = UltimaMensagem(
            usuario_1_id=self.usuarios_ids_ordenadas[0].id,
            usuario_2_id=self.usuarios_ids_ordenadas[1].id,
            mensagem_id=self.mensagem.id
        )
        ultima_mensagem.save()

        resultado = UltimaMensagem.trazer(
            usuario_1_id=self.usuario_origem.id,
            usuario_2_id=self.usuario_destino.id
        )

        self.assertEqual(resultado.mensagem_id, self.mensagem.id)

    def test_criar_ou_atualizar_QUADO_ultima_mensagem_existe_ENTAO_atualiza_mensagem_id(self) -> None:
        ultima_mensagem = UltimaMensagem(
            usuario_1_id=self.usuarios_ids_ordenadas[0].id,
            usuario_2_id=self.usuarios_ids_ordenadas[1].id,
            mensagem_id=self.mensagem.id
        )
        ultima_mensagem.save()
        nova_mensagem: Mensagem = FabricaTesteMensagem.create(
            origem_id=self.usuario_origem.id,
            destino_id=self.usuario_destino.id
        )

        UltimaMensagem.criar_ou_atualizar(
            usuario_1_id=self.usuario_origem.id,
            usuario_2_id=self.usuario_destino.id,
            mensagem_id=nova_mensagem.id
        )

        resultado = UltimaMensagem.objects.get(pk=ultima_mensagem.id)
        self.assertEqual(resultado.mensagem_id, nova_mensagem.id)

    def test_criar_ou_atualizar_QUADO_ultima_mensagem_nao_existe_ENTAO_cria_ultima_mensagem(self) -> None:
        UltimaMensagem.criar_ou_atualizar(
            usuario_1_id=self.usuario_origem.id,
            usuario_2_id=self.usuario_destino.id,
            mensagem_id=self.mensagem.id
        )

        resultado = UltimaMensagem.objects.all()[0]
        self.assertEqual(resultado.mensagem_id, self.mensagem.id)
