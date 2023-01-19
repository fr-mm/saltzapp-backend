from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class UltimaMensagemOTD:
    nome_outro_usuario: str
    id_outro_usuario: UUID
    enviada_em: datetime
    texto: str
