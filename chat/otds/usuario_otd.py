from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from chat.models import Usuario


@dataclass
class UsuarioOTD:
    id: UUID
    nome: str
    token: str

    @classmethod
    def de_modelo(cls, modelo: Usuario, token: str) -> UsuarioOTD:
        return cls(
            id=modelo.id,
            nome=modelo.username,
            token=token
        )
