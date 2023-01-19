from __future__ import annotations

from uuid import uuid4

from django.db import models

from chat.models.mensagem import Mensagem
from chat.models.usuario import Usuario


class UltimaMensagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    usuario_1 = models.ForeignKey(Usuario, related_name='usuario_1', on_delete=models.CASCADE)
    usuario_2 = models.ForeignKey(Usuario, related_name='usuario_2', on_delete=models.CASCADE)
    mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE)
