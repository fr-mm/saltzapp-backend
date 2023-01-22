from chat.mensagens_de_bot.mensagem_de_bot import MensagemDeBot
from chat.mensagens_de_bot.substituir import Substituir


class MensagemComSubstituicao(MensagemDeBot):
    REGEX_REPLACE_NOME = r'(\w ?)+'
    __texto: str
    __substituicao: Substituir
    __comparar_primeiros_caracteres: int

    def __init__(self, texto: str, substituicao: Substituir, comparar_primeiros_caracteres: int) -> None:
        self.__texto = texto
        self.__substituicao = substituicao
        self.__comparar_primeiros_caracteres = comparar_primeiros_caracteres

    def mesmo_tipo(self, texto: str) -> bool:
        return texto[:self.__comparar_primeiros_caracteres] == self.__texto[:self.__comparar_primeiros_caracteres]

    def texto(self, substituicao: str) -> str:
        return self.__texto.replace(self.__substituicao.antes, substituicao)

    @staticmethod
    def substituir(antes: str, regex: str) -> Substituir:
        return Substituir(antes, regex)
