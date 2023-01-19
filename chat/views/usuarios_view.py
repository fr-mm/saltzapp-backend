from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Usuario, Mensagem
from chat.otds import NovoUsuarioOTD
from chat.serializers import NovoUsuarioOTDSerializer


class UsuariosView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = NovoUsuarioOTDSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = NovoUsuarioOTD(**serializer.validated_data)
            usuario = Usuario.objects.create_user(
                username=otd.nome,
                password=otd.senha
            )
            outros_usuarios = [user for user in Usuario.objects.all() if user.id != usuario.id]
            for outro in outros_usuarios:
                Mensagem.criar(
                    origem_id=usuario.id,
                    destino_id=outro.id,
                    texto='Oi! Estou usando SaltZapp!'
                )
            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )
