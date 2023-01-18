from rest_framework import serializers


class NovaMensagemOTDSerializer(serializers.Serializer):
    origem_id = serializers.UUIDField()
    destino_id = serializers.UUIDField()
    texto = serializers.CharField(max_length=700)
