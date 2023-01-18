from uuid import uuid4

from django.db import models


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nome = models.CharField(max_length=50, unique=True)
    whatsapp = models.CharField(max_length=13, unique=True)
    divida = models.FloatField()
