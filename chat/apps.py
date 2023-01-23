from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chat"

    def ready(self) -> None:
        import string
        from random import choice

        from chat.models import Bot
        from chat.repositorios import UsuarioRepositorio

        bots = Bot.objects.all()
        [bot.usuario.delete() for bot in bots]
        bots.delete()
        usuario = UsuarioRepositorio.criar(
            nome='Saltzapp Bot',
            senha=''.join(choice(string.ascii_letters) for _ in range(10))
        )
        bot = Bot(usuario=usuario)
        bot.save()
