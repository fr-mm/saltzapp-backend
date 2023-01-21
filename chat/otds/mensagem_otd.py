from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from chat.models import Mensagem


@dataclass
class MensagemOTD:
    origem_id: UUID
    destino_id: UUID
    enviada_em: datetime
    texto: str

    @classmethod
    def de_modelo(cls, modelo: Mensagem) -> MensagemOTD:
        return MensagemOTD(
            origem_id=modelo.origem.id,
            destino_id=modelo.destino.id,
            enviada_em=modelo.enviada_em,
            texto=modelo.texto
        )

