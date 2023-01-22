from rest_framework import serializers

from chat.models import Cliente


class NovoClienteOTDSerializer(serializers.Serializer):
    nome = serializers.CharField(
        min_length=Cliente.config().NOME_TAMANHO_MINIMO,
        max_length=Cliente.config().NOME_TAMANHO_MAXIMO
    )
    whatsapp = serializers.CharField(
        min_length=Cliente.config().WHATSAPP_TAMANHO,
        max_length=Cliente.config().WHATSAPP_TAMANHO
    )
    divida = serializers.FloatField(
        min_value=Cliente.config().DIVIDA_VALOR_MINIMO
    )
