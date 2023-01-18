from rest_framework import serializers


class CadastroOTDSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=3, max_length=50)
    senha = serializers.CharField(min_length=6, max_length=50)
