from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Usuario
from chat.otds import NovoUsuarioOTD
from chat.serializers import NovoUsuarioOTDSerializer


class UsuariosView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = NovoUsuarioOTDSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = NovoUsuarioOTD(**serializer.validated_data)
            Usuario.objects.create_user(
                username=otd.nome,
                password=otd.senha
            )
            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )
