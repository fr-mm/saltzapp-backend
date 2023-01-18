from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Cliente
from chat.otds import NovoClienteOTD
from chat.serializers import NovoClienteOTDSerializer


class ClientesView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = NovoClienteOTDSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = NovoClienteOTD(**serializer.validated_data)
            cliente = Cliente(
                nome=otd.nome,
                whatsapp=otd.whatsapp,
                divida=otd.divida
            )
            cliente.save()
            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )
