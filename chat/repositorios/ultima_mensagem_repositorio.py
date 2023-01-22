from typing import List
from uuid import UUID

from django.db.models import Q

from chat.models import UltimaMensagem, Usuario, Mensagem


class UltimaMensagemRepositorio:
    @staticmethod
    def trazer_todas(usuario_id: UUID) -> List[UltimaMensagem]:
        ultimas_mensagens = UltimaMensagem.objects.filter(
            Q(usuario_1__id=usuario_id) | Q(usuario_2__id=usuario_id)
        )
        return sorted(ultimas_mensagens, key=lambda ultima_mensagem: ultima_mensagem.mensagem.enviada_em, reverse=True)

    @staticmethod
    def trazer_especifica(usuario_1_id: UUID, usuario_2_id: UUID) -> UltimaMensagem:
        return UltimaMensagem.objects.get(
            Q(usuario_1__id=usuario_1_id, usuario_2__id=usuario_2_id) |
            Q(usuario_1__id=usuario_2_id, usuario_2__id=usuario_1_id)
        )

    @staticmethod
    def criar(usuario_1: Usuario, usuario_2: Usuario, mensagem: Mensagem) -> UltimaMensagem:
        usuarios = sorted([usuario_1, usuario_2], key=lambda usuario: usuario.id)
        return UltimaMensagem.objects.create(
            usuario_1=usuarios[0],
            usuario_2=usuarios[1],
            mensagem=mensagem
        )
