from rest_framework import serializers


class MensagemOTDSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    origem_id = serializers.UUIDField()
    destino_id = serializers.UUIDField()
    enviada_em = serializers.DateTimeField()
    texto = serializers.CharField(max_length=700)
