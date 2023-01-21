from typing import List
from uuid import UUID

from django.db.models import Q

from chat.models import Mensagem, Usuario


class MensagemRepositorio:
    @staticmethod
    def trazer(usuario_1_id: UUID, usuario_2_id: UUID) -> List[Mensagem]:
        usuario_1 = Usuario.objects.get(pk=usuario_1_id)
        outro_2 = Usuario.objects.get(pk=usuario_2_id)
        mensagens = Mensagem.objects.filter(
            Q(origem=usuario_1, destino=outro_2) | Q(origem=outro_2, destino=usuario_1)
        )
        return sorted(mensagens, key=lambda mensagem: mensagem.enviada_em)

