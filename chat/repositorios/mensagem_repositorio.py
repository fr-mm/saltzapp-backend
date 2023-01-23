from typing import List
from uuid import UUID

from django.db.models import Q

from chat.models import Mensagem, Usuario, UltimaMensagem
from chat.repositorios.ultima_mensagem_repositorio import UltimaMensagemRepositorio


class MensagemRepositorio:
    @staticmethod
    def criar_sem_salvar(origem_id: UUID, destino_id: UUID, texto: str) -> Mensagem:
        origem = Usuario.objects.get(pk=origem_id)
        destino = Usuario.objects.get(pk=destino_id)
        return Mensagem(
            origem=origem,
            destino=destino,
            texto=texto
        )

    @staticmethod
    def salvar(mensagem: Mensagem) -> Mensagem:
        mensagem.save()
        ultima_mensagem: UltimaMensagem
        try:
            ultima_mensagem = UltimaMensagemRepositorio.trazer_especifica(
                usuario_1_id=mensagem.origem.id,
                usuario_2_id=mensagem.destino.id
            )
            ultima_mensagem.mensagem = mensagem
            ultima_mensagem.save()
        except UltimaMensagem.DoesNotExist:
            UltimaMensagemRepositorio.criar(
                usuario_1=mensagem.origem,
                usuario_2=mensagem.destino,
                mensagem=mensagem
            )
        return mensagem

    @staticmethod
    def criar(origem_id: UUID, destino_id: UUID, texto: str) -> Mensagem:
        mensagem = MensagemRepositorio.criar_sem_salvar(origem_id, destino_id, texto)
        return MensagemRepositorio.salvar(mensagem)

    @staticmethod
    def trazer_conversa(usuario_1_id: UUID, usuario_2_id: UUID) -> List[Mensagem]:
        usuario_1 = Usuario.objects.get(pk=usuario_1_id)
        outro_2 = Usuario.objects.get(pk=usuario_2_id)
        mensagens = Mensagem.objects.filter(
            Q(origem=usuario_1, destino=outro_2) | Q(origem=outro_2, destino=usuario_1)
        )
        return sorted(mensagens, key=lambda mensagem: mensagem.enviada_em, reverse=True)
