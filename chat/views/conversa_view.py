from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.otds import MensagemOTD, UltimaMensagemOTD
from chat.repositorios import MensagemRepositorio, UltimaMensagemRepositorio
from chat.serializers import MensagemOTDSerializer, UltimaMensagemOTDSerializer


class ConversaView(APIView):
    def get(self, _: Request, usuario_id: UUID, destino_id: UUID) -> Response:
        mensagens = MensagemRepositorio.trazer(usuario_id, destino_id)
        ultimas_mensagens = UltimaMensagemRepositorio.trazer(usuario_id)
        mensagens_otds = [MensagemOTD.de_modelo(mensagem) for mensagem in mensagens]
        ultimas_mensagens_otds = [UltimaMensagemOTD.de_modelo(ultima_mensagem, usuario_id) for ultima_mensagem in ultimas_mensagens]
        mensagens_serializer = MensagemOTDSerializer(mensagens_otds, many=True)
        ultimas_mensagens_serializer = UltimaMensagemOTDSerializer(ultimas_mensagens_otds, many=True)

        return Response(
            data={
                'mensagens': mensagens_serializer.data,
                'ultimas_mensagens': ultimas_mensagens_serializer.data
            },
            status=200
        )
