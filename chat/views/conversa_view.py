from typing import List
from uuid import UUID

from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Usuario, Mensagem
from chat.otds import MensagemOTD
from chat.serializers import MensagemOTDSerializer


class ConversaView(APIView):
    def get(self, request: Request, usuario_id: UUID, destino_id: UUID) -> Response:
        mensagens = self.__trazer_mensagens(usuario_id, destino_id)
        otds = [self.__mensagem_para_otd(mensagem) for mensagem in mensagens]
        otds.sort(key=lambda otd: otd.enviada_em)
        serializer = MensagemOTDSerializer(otds, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

    @staticmethod
    def __trazer_mensagens(usuario_id: UUID, outro_usuario_id: UUID) -> List[Mensagem]:
        usuario = Usuario.objects.get(pk=usuario_id)
        outro_usuario = Usuario.objects.get(pk=outro_usuario_id)
        return Mensagem.objects.filter(
            Q(origem=usuario, destino=outro_usuario) | Q(origem=outro_usuario, destino=usuario)
        )

    @staticmethod
    def __mensagem_para_otd(mensagem: Mensagem) -> MensagemOTD:
        return MensagemOTD(
            origem_id=mensagem.origem.id,
            destino_id=mensagem.destino.id,
            enviada_em=mensagem.enviada_em,
            texto=mensagem.texto
        )
