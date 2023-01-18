from django.db import models


class Funcionario(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=24)
