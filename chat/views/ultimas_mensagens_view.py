from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.otds import UltimaMensagemOTD
from chat.repositorios import UltimaMensagemRepositorio
from chat.serializers import UltimaMensagemOTDSerializer


class UltimasMensagemsView(APIView):
    def get(self, _: Request, usuario_id: UUID) -> Response:
        ultimas_mensagens = UltimaMensagemRepositorio.trazer(usuario_id)
        otds = [UltimaMensagemOTD.de_modelo(ultima_mensagem, usuario_id) for ultima_mensagem in ultimas_mensagens]
        serializer = UltimaMensagemOTDSerializer(otds, many=True)

        return Response(
            data=serializer.data,
            status=200
        )
