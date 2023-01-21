from dataclasses import dataclass

from rest_framework import serializers


@dataclass(frozen=True)
class Limites:
    tamanho_minimo: int
    tamanho_maximo: int


@dataclass(frozen=True, init=False)
class LimitesDeAtributos:
    nome = Limites(
        tamanho_minimo=3,
        tamanho_maximo=50
    )
    senha = Limites(
        tamanho_minimo=4,
        tamanho_maximo=50
    )


class NovoUsuarioOTDSerializer(serializers.Serializer):
    nome = serializers.CharField(
        min_length=LimitesDeAtributos.nome.tamanho_minimo,
        max_length=LimitesDeAtributos.nome.tamanho_maximo
    )
    senha = serializers.CharField(
        min_length=LimitesDeAtributos.senha.tamanho_minimo,
        max_length=LimitesDeAtributos.senha.tamanho_maximo
    )

    @classmethod
    def limites(cls) -> LimitesDeAtributos:
        return LimitesDeAtributos()
