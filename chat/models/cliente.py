from django.db import models


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    whatsapp = models.CharField(max_length=13, unique=True)
    divida = models.FloatField()
