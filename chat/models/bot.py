from __future__ import annotations

from uuid import uuid4

from djongo import models

from chat.models.usuario import Usuario


class Bot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    @classmethod
    def trazer(cls) -> Bot:
        bots = Bot.objects.all()

        if 0 < len(bots) < 2:
            return bots[0]
        else:
            raise Exception('Só deveria existir 1 bot')
