from typing import List
from uuid import UUID

from django.db.models import Q

from chat.models import UltimaMensagem, Usuario


class UltimaMensagemRepositorio:
    @staticmethod
    def trazer(usuario_id: UUID) -> List[UltimaMensagem]:
        usuario: Usuario = Usuario.objects.get(pk=usuario_id)
        ultimas_mensagens = UltimaMensagem.objects.filter(
            Q(usuario_1=usuario) | Q(usuario_2=usuario)
        )
        return sorted(ultimas_mensagens, key=lambda ultima_mensagem: ultima_mensagem.mensagem.enviada_em, reverse=True)
