from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.otds import NovaMensagemOTD
from chat.repositorios import MensagemRepositorio
from chat.serializers import NovaMensagemOTDSerializer
from chat.servicos import BotServico


class MensagensView(APIView):
    __bot_servico = BotServico()

    def post(self, request: Request) -> Response:
        try:
            serializer = NovaMensagemOTDSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = NovaMensagemOTD(**serializer.validated_data)
            mensagem = MensagemRepositorio.criar_sem_salvar(
                origem_id=otd.origem_id,
                destino_id=otd.destino_id,
                texto=otd.texto
            )
            resposta_do_bot = self.__bot_servico.analisar_mensagem(mensagem)
            MensagemRepositorio.salvar(mensagem)
            if resposta_do_bot:
                MensagemRepositorio.salvar(resposta_do_bot)

            return Response(
                status=201
            )

        except ValidationError:
            return Response(
                status=400
            )
