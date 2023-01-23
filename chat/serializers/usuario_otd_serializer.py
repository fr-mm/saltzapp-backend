from rest_framework import serializers


class UsuarioOTDSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField()
    token = serializers.CharField()
