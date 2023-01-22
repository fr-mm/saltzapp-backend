from uuid import uuid4

from djongo import models

from chat.models.cliente import Cliente
from chat.models.usuario import Usuario


class ClienteEmCriacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=Cliente.config().NOME_TAMANHO_MAXIMO, unique=True, null=True)
    whatsapp = models.CharField(max_length=Cliente.config().WHATSAPP_TAMANHO, unique=True, null=True)
    divida = models.FloatField(null=True)
