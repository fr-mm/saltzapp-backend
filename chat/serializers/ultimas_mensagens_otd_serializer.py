from rest_framework import serializers


class UltimaMensagemOTDSerializer(serializers.Serializer):
    nome_outro_usuario = serializers.CharField(min_length=3, max_length=50)
    id_outro_usuario = serializers.UUIDField()
    enviada_em = serializers.DateTimeField()
    texto = serializers.CharField(max_length=700)
