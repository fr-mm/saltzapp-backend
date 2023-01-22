from dataclasses import dataclass


@dataclass(frozen=True)
class Substituir:
    antes: str
    depois: str
