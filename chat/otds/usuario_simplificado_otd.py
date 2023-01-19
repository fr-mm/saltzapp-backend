from dataclasses import dataclass
from uuid import UUID


@dataclass
class UsuarioSimplificadoOTD:
    id: UUID
    nome: str
