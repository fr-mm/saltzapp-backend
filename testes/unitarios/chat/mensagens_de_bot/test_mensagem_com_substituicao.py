from unittest import TestCase

from chat.mensagens_de_bot.mensagem_com_substituicao import MensagemComSubstituicao


class TestMensagemComSubstituicao(TestCase):
    def test_mesmo_tipo_QUANDO_verdadeiro_ENTAO_retorna_true(self) -> None:
        msg = MensagemComSubstituicao(
            texto='Oi {nome}, tudo bem?\nTudo!',
            substituicao=MensagemComSubstituicao.substituir('{nome}', MensagemComSubstituicao.REGEX_REPLACE_NOME),
            comparar_primeiros_caracteres=3
        )
        texto = msg.texto('outra coisa')

        mesmo_tipo = msg.mesmo_tipo(texto)

        self.assertTrue(mesmo_tipo)

    def test_mesmo_tipo_QUANDO_falso_ENTAO_retorna_false(self) -> None:
        msg = MensagemComSubstituicao(
            texto='Oi {nome}, tudo bem?\nTudo!',
            substituicao=MensagemComSubstituicao.substituir('{nome}', MensagemComSubstituicao.REGEX_REPLACE_NOME),
            comparar_primeiros_caracteres=3
        )

        mesmo_tipo = msg.mesmo_tipo('Outro texto')

        self.assertFalse(mesmo_tipo)
    
    def test_mesmo_tipo_QUANDO_mensagem_de_intro_ENTAO_reconhece(self) -> None:
        msg = MensagemComSubstituicao(
            texto='Olá {nome}! Como posso ajudar? (digite 0 a qualquer momento para cancelar a operação) 1 - cadastrar cliente 2 - cobrar clientes',
            substituicao=MensagemComSubstituicao.substituir('{nome}', MensagemComSubstituicao.REGEX_REPLACE_NOME),
            comparar_primeiros_caracteres=3
        )
        texto = 'Olá chico! Como posso ajudar? (digite 0 a qualquer momento para cancelar a operação) 1 - cadastrar cliente 2 - cobrar clientes'

        mesmo_tipo = msg.mesmo_tipo(texto)

        self.assertTrue(mesmo_tipo)
