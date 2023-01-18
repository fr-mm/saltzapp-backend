from django.db import models


class Bot(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=50)
