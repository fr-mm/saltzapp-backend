from dataclasses import dataclass


@dataclass
class NovoClienteOTD:
    nome: str
    whatsapp: str
    divida: float
