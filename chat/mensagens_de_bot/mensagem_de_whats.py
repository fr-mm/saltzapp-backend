from chat.mensagens_de_bot.substituir import Substituir


class MensagemDeWhats:
    __texto: str

    def __init__(self, texto: str) -> None:
        self.__texto = texto

    def texto(self, **kwargs: str) -> str:
        texto = self.__texto
        for antes in kwargs.keys():
            texto = texto.replace(f'{{{antes}}}', kwargs[antes])
        return texto

    @staticmethod
    def substituir(antes: str, depois: str) -> Substituir:
        return Substituir(antes, depois)
