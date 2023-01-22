from abc import ABC, abstractmethod


class MensagemDeBot(ABC):
    @abstractmethod
    def mesmo_tipo(self, texto: str) -> bool:
        pass

    @abstractmethod
    def texto(self, *args) -> str:
        pass
