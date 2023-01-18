from dataclasses import dataclass
from uuid import UUID


@dataclass
class NovaMensagemOTD:
    origem_id: UUID
    destino_id: UUID
    texto: str
