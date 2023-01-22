from uuid import UUID

from chat.models import Usuario
from chat.repositorios.mensagem_repositorio import MensagemRepositorio


class UsuarioRepositorio:
    @staticmethod
    def criar(nome: str, senha: str) -> Usuario:
        usuario = Usuario.criar(nome, senha)
        outros_usuarios = [user for user in Usuario.objects.all() if user.id != usuario.id]
        for outro_usuario in outros_usuarios:
            MensagemRepositorio.criar(
                origem_id=usuario.id,
                destino_id=outro_usuario.id,
                texto='Oi! Estou usando SaltZapp!'
            )
        return usuario

    @staticmethod
    def trazer(id_: UUID) -> Usuario:
        return Usuario.objects.get(pk=id_)
