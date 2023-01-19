from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Mensagem, Usuario, UltimaMensagem
from chat.otds import NovaMensagemOTD
from chat.serializers import NovaMensagemOTDSerializer


class MensagemsView(APIView):
    def post(self, request: Request) -> Response:
        try:
            mensagem = self.__criar_mensagem(request)
            self.__atualizar_ultima_mensagem(mensagem)

            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )

    @staticmethod
    def __criar_mensagem(request: Request) -> Mensagem:
        serializer = NovaMensagemOTDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otd = NovaMensagemOTD(**serializer.validated_data)
        origem = Usuario.objects.get(pk=otd.origem_id)
        destino = Usuario.objects.get(pk=otd.destino_id)
        mensagem = Mensagem(
            origem=origem,
            destino=destino,
            texto=otd.texto
        )
        mensagem.save()
        return mensagem

    @staticmethod
    def __atualizar_ultima_mensagem(mensagem: Mensagem) -> None:
        usuarios = sorted([mensagem.origem, mensagem.destino], key=lambda usuario: usuario.id)
        ultima_mensagem: UltimaMensagem = UltimaMensagem.objects.get(
            usuario_1=usuarios[0],
            usuario_2=usuarios[1]
        )
        ultima_mensagem.mensagem = mensagem
        ultima_mensagem.save()
