from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Usuario, Mensagem, UltimaMensagem
from chat.otds import NovoUsuarioOTD
from chat.serializers import NovoUsuarioOTDSerializer


class UsuariosView(APIView):
    def post(self, request: Request) -> Response:
        try:
            usuario = self.__criar_usuario(request)
            self.__criar_mensagem_padrao(usuario)
            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )

    @staticmethod
    def __criar_usuario(request: Request) -> Usuario:
        serializer = NovoUsuarioOTDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otd = NovoUsuarioOTD(**serializer.validated_data)
        return Usuario.objects.create_user(
            username=otd.nome,
            password=otd.senha
        )

    @staticmethod
    def __criar_mensagem_padrao(usuario: Usuario) -> None:
        outros_usuarios = [user for user in Usuario.objects.all() if user.id != usuario.id]
        for outro_usuario in outros_usuarios:
            mensagem = Mensagem(
                origem_id=usuario.id,
                destino_id=outro_usuario.id,
                texto='Oi! Estou usando SaltZapp!'
            )
            mensagem.save()
            usuarios = sorted([usuario, outro_usuario], key=lambda user: user.id)
            UltimaMensagem(
                usuario_1=usuarios[0],
                usuario_2=usuarios[1],
                mensagem=mensagem
            ).save()
