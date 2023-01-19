from __future__ import annotations

from uuid import uuid4

from djongo import models

from chat.models.usuario import Usuario


class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    enviada_em = models.DateTimeField(auto_now=True)
    origem = models.ForeignKey(Usuario, related_name='origem', on_delete=models.CASCADE)
    destino = models.ForeignKey(Usuario, related_name='destino', on_delete=models.CASCADE)
    texto = models.CharField(max_length=700, editable=False)
