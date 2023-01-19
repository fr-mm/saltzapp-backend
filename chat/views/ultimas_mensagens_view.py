from typing import List
from uuid import UUID

from django.db.models import Q
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import UltimaMensagem
from chat.otds import UltimaMensagemOTD, UsuarioSimplificadoOTD


class UltimasMensagemsView(APIView):
    def get(self, request: Request, usuario_id: UUID) -> Response:
        ultimas_mensagens: List[UltimaMensagem] = UltimaMensagem.objects.filter(
            Q(usuario_1_id=usuario_id) | Q(usuario_2_id=usuario_id)
        )
        otds = []
        for ultima_mensagem in ultimas_mensagens:
            outro_usuario: UsuarioSimplificadoOTD
            if ultima_mensagem.usuario_1_id == ultima_mensagem:
                outro_usuario = UsuarioSimplificadoOTD(
                    id=ultima_mensagem.usuario_2_id,
                    nome=ultima_mensagem.usuario_2_nome
                )
            else:
                outro_usuario = UsuarioSimplificadoOTD(
                    id=ultima_mensagem.usuario_1_id,
                    nome=ultima_mensagem.usuario_1_nome
                )
            ultima_mensagem_ods = UltimaMensagemOTD(
                nome_outro_usuario=outro_usuario.nome,
                id_outro_usuario=outro_usuario.id,
                texto=ultima_mensagem.texto
            )
            otds.append(ultima_mensagem_ods)
        otds.sort(key=lambda otd: otd.enviada_em)
