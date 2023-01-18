from datetime import datetime
from uuid import uuid4

from django.db import models


class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    enviada_em = models.DateTimeField(default=datetime.now, editable=False)
    origem_id = models.UUIDField(editable=False)
    destino_id = models.UUIDField(editable=False)
    texto = models.CharField(max_length=700, editable=False)
