from typing import List
from uuid import UUID

from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import UltimaMensagem, Usuario
from chat.otds import UltimaMensagemOTD


class UltimasMensagemsView(APIView):
    def get(self, request: Request, usuario_id: UUID) -> Response:
        usuario: Usuario = Usuario.objects.get(pk=usuario_id)
        ultimas_mensagens: List[UltimaMensagem] = UltimaMensagem.objects.filter(
            Q(usuario_1=usuario) | Q(usuario_2=usuario)
        )
        ultimas_mensagens.sort(key=lambda ultima: ultima.mensagem.enviada_em)
        otds = []
        for ultima_mensagem in ultimas_mensagens:
            nome_outro_usuario: str
            id_outro_usuario: UUID
            if ultima_mensagem.usuario_1.id == usuario_id:
                nome_outro_usuario = ultima_mensagem.usuario_2.nome
                id_outro_usuario = ultima_mensagem.usuario_2.id
            else:
                nome_outro_usuario = ultima_mensagem.usuario_1.nome
                id_outro_usuario = ultima_mensagem.usuario_1.id
            otd = UltimaMensagemOTD(
                nome_outro_usuario=nome_outro_usuario,
                id_outro_usuario=id_outro_usuario,
                enviada_em=ultima_mensagem.mensagem.enviada_em,
                texto=ultima_mensagem.mensagem.texto
            )
            otds.append(otd)
        otds.sort(key=lambda otd_: otd_.enviada_em)

