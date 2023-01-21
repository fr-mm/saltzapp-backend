from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.otds import MensagemOTD
from chat.repositorios import MensagemRepositorio
from chat.serializers import MensagemOTDSerializer


class ConversaView(APIView):
    def get(self, _: Request, usuario_id: UUID, destino_id: UUID) -> Response:
        mensagens = MensagemRepositorio.trazer(usuario_id, destino_id)
        otds = [MensagemOTD.de_modelo(mensagem) for mensagem in mensagens]
        serializer = MensagemOTDSerializer(otds, many=True)

        return Response(
            data=serializer.data,
            status=200
        )
