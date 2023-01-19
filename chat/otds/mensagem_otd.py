from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class MensagemOTD:
    origem_id: UUID
    destino_id: UUID
    enviada_em: datetime
    texto: str
