from uuid import uuid4

from django.db import models


class Bot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nome = models.CharField(max_length=50)
