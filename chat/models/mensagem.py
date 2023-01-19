from __future__ import annotations

from uuid import uuid4, UUID

from django.db import models

from chat.models.ultima_mensagem import UltimaMensagem


class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    enviada_em = models.DateTimeField(auto_now=True)
    origem_id = models.UUIDField(editable=False)
    destino_id = models.UUIDField(editable=False)
    texto = models.CharField(max_length=700, editable=False)

    @classmethod
    def criar(cls, origem_id: UUID, destino_id: UUID, texto: str) -> Mensagem:
        mensagem = Mensagem(
            origem_id=origem_id,
            destino_id=destino_id,
            texto=texto
        )
        mensagem.save()
        UltimaMensagem.criar_ou_atualizar(
            usuario_1_id=origem_id,
            usuario_2_id=destino_id,
            texto=texto
        )
        return mensagem
