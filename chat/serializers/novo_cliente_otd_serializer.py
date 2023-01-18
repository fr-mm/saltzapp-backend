from rest_framework import serializers


class NovoClienteOTDSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=3, max_length=50)
    whatsapp = serializers.CharField(min_length=13, max_length=13)
    divida = serializers.FloatField(min_value=0)
