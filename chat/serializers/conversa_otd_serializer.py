from __future__ import annotations

from rest_framework import serializers

from chat.serializers.mensagem_otd_serializer import MensagemOTDSerializer
from chat.serializers.ultima_mensagem_otd_serializer import UltimaMensagemOTDSerializer


class ConversaOTDSerializer(serializers.Serializer):
    mensagens = MensagemOTDSerializer(many=True)
    ultimas_mensagens = UltimaMensagemOTDSerializer(many=True)
