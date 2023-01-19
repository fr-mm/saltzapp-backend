from typing import List
from uuid import UUID

from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import UltimaMensagem, Usuario
from chat.otds import UltimaMensagemOTD
from chat.serializers import UltimaMensagemOTDSerializer


class UltimasMensagemsView(APIView):
    def get(self, request: Request, usuario_id: UUID) -> Response:
        ultimas_mensagens = self.__trazer_ultimas_mensagens(usuario_id)
        otds = [self.__ultima_mensagem_para_otd(ultima_mensagem, usuario_id) for ultima_mensagem in ultimas_mensagens]
        otds.sort(key=lambda otd_: otd_.enviada_em, reverse=True)
        serializer = UltimaMensagemOTDSerializer(otds, many=True)

        return Response(
            data=serializer.data,
            status=200
        )

    @staticmethod
    def __trazer_ultimas_mensagens(usuario_id: UUID) -> List[UltimaMensagem]:
        usuario: Usuario = Usuario.objects.get(pk=usuario_id)
        return UltimaMensagem.objects.filter(
            Q(usuario_1=usuario) | Q(usuario_2=usuario)
        )

    @staticmethod
    def __ultima_mensagem_para_otd(ultima_mensagem: UltimaMensagem, usuario_id: UUID) -> UltimaMensagemOTD:
        nome_outro_usuario: str
        id_outro_usuario: UUID
        if ultima_mensagem.usuario_1.id == usuario_id:
            nome_outro_usuario = ultima_mensagem.usuario_2.username
            id_outro_usuario = ultima_mensagem.usuario_2.id
        else:
            nome_outro_usuario = ultima_mensagem.usuario_1.username
            id_outro_usuario = ultima_mensagem.usuario_1.id
        return UltimaMensagemOTD(
            nome_outro_usuario=nome_outro_usuario,
            id_outro_usuario=id_outro_usuario,
            enviada_em=ultima_mensagem.mensagem.enviada_em,
            texto=ultima_mensagem.mensagem.texto
        )
