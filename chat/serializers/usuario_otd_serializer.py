from rest_framework import serializers


class UsuarioOTDSerializer(serializers.Serializer):
    nome = serializers.CharField()
    token = serializers.CharField()
