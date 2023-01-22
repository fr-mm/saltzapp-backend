from unittest import TestCase

from chat.mensagens_de_bot import MensagemSimples


class TestMensagemSimples(TestCase):
    def test_mesmo_tipo_QUANDO_verdadeiro_ENTAO_retorna_true(self) -> None:
        texto = 'Qual o whatsapp do(a) cliente?'
        msg = MensagemSimples(texto)

        mesmo_tipo = msg.mesmo_tipo(texto)

        self.assertTrue(mesmo_tipo)
