from chat.mensagens_de_bot.mensagem_de_bot import MensagemDeBot


class MensagemSimples(MensagemDeBot):
    __TEXTO: str

    def __init__(self, texto: str) -> None:
        self.__TEXTO = texto

    def mesmo_tipo(self, texto: str) -> bool:
        return self.__TEXTO == texto

    def texto(self) -> str:
        return self.__TEXTO
