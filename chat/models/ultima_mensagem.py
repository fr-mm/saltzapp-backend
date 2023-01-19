from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from django.db import models

from chat.models.mensagem import Mensagem
from chat.models.usuario import Usuario
from chat.otds import UsuarioSimplificadoOTD


class UltimaMensagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    usuario_1 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario_2 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE)
    """
    usuario_1_id = models.UUIDField(editable=False)
    usuario_1_nome = models.CharField(max_length=50, editable=False, null=True)
    usuario_2_id = models.UUIDField(editable=False)
    usuario_2_nome = models.CharField(max_length=50, editable=False, null=True)
    enviada_em = models.DateField(null=True)
    texto = models.CharField(max_length=700, null=True)
    """

    @classmethod
    def trazer(cls, usuario_1_id: UUID, usuario_2_id: UUID) -> UltimaMensagem:
        ids = sorted([usuario_1_id, usuario_2_id])
        return UltimaMensagem.objects.get(
            usuario_1_id=ids[0],
            usuario_2_id=ids[1]
        )

    @classmethod
    def criar_ou_atualizar(
            cls,
            usuario_1_id: UUID,
            usuario_1_nome: str,
            usuario_2_id: UUID,
            usuario_2_nome: str,
            enviada_em: datetime,
            texto: str
    ) -> UltimaMensagem:
        ultima_mensagem: UltimaMensagem

        try:
            ultima_mensagem = cls.trazer(usuario_1_id, usuario_2_id)
            ultima_mensagem.enviada_em = enviada_em
            ultima_mensagem.texto = texto

        except UltimaMensagem.DoesNotExist:
            usuarios = [
                UsuarioSimplificadoOTD(id=usuario_1_id, nome=usuario_1_nome),
                UsuarioSimplificadoOTD(id=usuario_2_id, nome=usuario_2_nome)
            ]
            usuarios.sort(key=lambda usuario: usuario.id)
            ultima_mensagem = UltimaMensagem(
                usuario_1_id=usuarios[0].id,
                usuario_1_nome=usuarios[0].nome,
                usuario_2_id=usuarios[1].id,
                usuario_2_nome=usuarios[1].nome,
                enviada_em=enviada_em,
                texto=texto
            )

        ultima_mensagem.save()
        return ultima_mensagem
