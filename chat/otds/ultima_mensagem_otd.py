from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from chat.models import UltimaMensagem


@dataclass
class UltimaMensagemOTD:
    id: UUID
    nome_outro_usuario: str
    id_outro_usuario: UUID
    enviada_em: datetime
    texto: str

    @classmethod
    def de_modelo(cls, modelo: UltimaMensagem, usuario_id: UUID) -> UltimaMensagemOTD:
        nome_outro_usuario: str
        id_outro_usuario: UUID
        if modelo.usuario_1.id == usuario_id:
            nome_outro_usuario = modelo.usuario_2.username
            id_outro_usuario = modelo.usuario_2.id
        else:
            nome_outro_usuario = modelo.usuario_1.username
            id_outro_usuario = modelo.usuario_1.id
        return UltimaMensagemOTD(
            id=modelo.id,
            nome_outro_usuario=nome_outro_usuario,
            id_outro_usuario=id_outro_usuario,
            enviada_em=modelo.mensagem.enviada_em,
            texto=modelo.mensagem.texto
        )
