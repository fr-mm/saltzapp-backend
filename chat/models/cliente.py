from dataclasses import dataclass
from uuid import uuid4

from djongo import models


@dataclass(frozen=True, init=False)
class Limites:
    NOME_TAMANHO_MINIMO = 3
    NOME_TAMANHO_MAXIMO = 50
    WHATSAPP_TAMANHO = 13
    DIVIDA_VALOR_MINIMO = 0


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nome = models.CharField(max_length=Limites.NOME_TAMANHO_MAXIMO, unique=True)
    whatsapp = models.CharField(max_length=Limites.WHATSAPP_TAMANHO, unique=True)
    divida = models.FloatField()

    @staticmethod
    def config() -> Limites:
        return Limites()
