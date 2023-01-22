from chat.mensagens_de_bot.mensagem_de_bot import MensagemDeBot


class PerguntaWhatsCliente(MensagemDeBot):
    __TEXTO = 'Qual o whatsapp do cliente?'

    def mesmo_tipo(self, texto: str) -> bool:
        return texto == texto

    def texto(self) -> str:
        return PerguntaWhatsCliente.__TEXTO
