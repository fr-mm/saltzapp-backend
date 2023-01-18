from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Mensagem
from chat.otds import NovaMensagemOTD
from chat.serializers import NovaMensagemOTDSerializer


class MensagemsView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = NovaMensagemOTDSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = NovaMensagemOTD(**serializer.validated_data)
            mensagem = Mensagem(
                origem_id=otd.origem_id,
                destino_id=otd.destino_id,
                texto=otd.texto
            )
            mensagem.save()
            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )
