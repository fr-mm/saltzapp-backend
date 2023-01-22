import string
from random import choice

from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chat"

    def ready(self) -> None:
        from chat.models import Bot
        from chat.repositorios import UsuarioRepositorio

        bots = Bot.objects.all()
        if not bots:
            usuario = UsuarioRepositorio.criar(
                nome='Saltzapp Bot',
                senha=''.join(choice(string.ascii_letters) for _ in range(10))
            )
            bot = Bot(usuario=usuario)
            bot.save()
        if len(bots) > 1:
            raise Exception('Só deveria existir 1 bot')
