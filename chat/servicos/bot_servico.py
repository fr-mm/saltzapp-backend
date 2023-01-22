import re

from chat import mensagens_de_bot
from chat.models import Bot, Mensagem, UltimaMensagem, Cliente
from chat.repositorios import UltimaMensagemRepositorio, MensagemRepositorio, UsuarioRepositorio
from chat.repositorios.cliente_em_cliacao_repositorio import ClienteEmCriacaoRepositorio


class BotServico:
    __bot = Bot.trazer()
    __mensagem: Mensagem
    __texto_da_mensagem: str
    __ultima_mensagem: UltimaMensagem
    __texto_da_ultima_mensagem: str

    def analisar_mensagem(self, mensagem: Mensagem) -> Mensagem or None:
        if mensagem.destino == BotServico.__bot.usuario:
            self.__mensagem = mensagem
            self.__texto_da_mensagem = mensagem.texto.strip()
            self.__ultima_mensagem = UltimaMensagemRepositorio.trazer_especifica(
                self.__mensagem.origem.id,
                self.__mensagem.destino.id
            )
            self.__texto_da_ultima_mensagem = self.__ultima_mensagem.mensagem.texto.strip()
            return self.__responder()

    def __responder(self) -> Mensagem:
        if mensagens_de_bot.intro.mesmo_tipo(self.__texto_da_ultima_mensagem):
            return self.__processar_resposta_de_intro()
        elif self.__texto_da_mensagem == '0':
            return self.__encerrar_atendimento()
        elif mensagens_de_bot.pergunta_whats_do_cliente.mesmo_tipo(self.__texto_da_ultima_mensagem) or \
                mensagens_de_bot.whats_invalido.mesmo_tipo(self.__texto_da_ultima_mensagem):
            return self.__processar_whats_de_cliente()
        elif mensagens_de_bot.pergunta_nome_do_cliente.mesmo_tipo(self.__texto_da_ultima_mensagem) or \
                mensagens_de_bot.nome_invalido.mesmo_tipo(self.__texto_da_ultima_mensagem):
            return self.__processar_nome_de_cliente()
        elif mensagens_de_bot.pergunta_divida_do_cliente.mesmo_tipo(self.__texto_da_ultima_mensagem) or \
                mensagens_de_bot.divida_invalida.mesmo_tipo(self.__texto_da_ultima_mensagem):
            return self.__processar_divida_de_cliente()
        else:
            return self.__criar_resposta(mensagens_de_bot.intro.texto(self.__mensagem.origem.username))

    def __processar_resposta_de_intro(self) -> Mensagem:
        if self.__texto_da_mensagem == '0':
            return self.__encerrar_atendimento()
        elif self.__texto_da_mensagem == '1':
            ClienteEmCriacaoRepositorio.criar(criador=self.__mensagem.origem)
            return self.__criar_resposta(
                texto=mensagens_de_bot.pergunta_whats_do_cliente.texto()
            )
        elif self.__texto_da_mensagem == '2':
            return self.__criar_resposta(
                texto='TBD'
            )
        else:
            return self.__criar_resposta(
                texto=mensagens_de_bot.intro.texto(self.__mensagem.origem.username)
            )

    def __processar_whats_de_cliente(self) -> Mensagem:
        if self.__texto_da_mensagem == '0':
            return self.__encerrar_atendimento()

        if self.__texto_da_mensagem.isnumeric() and len(self.__texto_da_mensagem) == Cliente.config().WHATSAPP_TAMANHO:
            ClienteEmCriacaoRepositorio.editar(criador=self.__mensagem.origem, whatsapp=self.__texto_da_mensagem)
            return self.__criar_resposta(
                texto=mensagens_de_bot.pergunta_nome_do_cliente.texto()
            )
        else:
            return self.__criar_resposta(
                texto=mensagens_de_bot.whats_invalido.texto()
            )

    def __processar_nome_de_cliente(self) -> Mensagem:
        if self.__texto_da_mensagem == '0':
            return self.__encerrar_atendimento()

        if Cliente.config().NOME_TAMANHO_MINIMO <= len(self.__texto_da_mensagem) <= Cliente.config().NOME_TAMANHO_MAXIMO:
            ClienteEmCriacaoRepositorio.editar(criador=self.__mensagem.origem, nome=self.__texto_da_mensagem)
            return self.__criar_resposta(
                texto=mensagens_de_bot.pergunta_divida_do_cliente.texto()
            )
        else:
            return self.__criar_resposta(
                texto=mensagens_de_bot.nome_invalido.texto()
            )

    def __processar_divida_de_cliente(self) -> Mensagem:
        if self.__texto_da_mensagem == '0':
            return self.__encerrar_atendimento()

        try:
            divida = float(self.__texto_da_mensagem)
            if divida >= Cliente.config().DIVIDA_VALOR_MINIMO:
                cliente_em_criacao = ClienteEmCriacaoRepositorio.editar(criador=self.__mensagem.origem, divida=divida)
                cliente = ClienteEmCriacaoRepositorio.transformar_em_cliente(cliente_em_criacao)
                return self.__criar_resposta(
                    texto=mensagens_de_bot.cliente_cadastrado.texto(cliente.nome)
                )
            else:
                raise ValueError()
        except ValueError:
            return self.__criar_resposta(
                texto=mensagens_de_bot.divida_invalida.texto()
            )

    def __encerrar_atendimento(self) -> Mensagem:
        ClienteEmCriacaoRepositorio.deletar_por_criador(self.__mensagem.origem)
        return self.__criar_resposta(
            texto=mensagens_de_bot.atendimento_encerrado.texto()
        )

    def __criar_resposta(self, texto: str) -> Mensagem:
        return MensagemRepositorio.criar(
            origem_id=BotServico.__bot.usuario.id,
            destino_id=self.__mensagem.origem.id,
            texto=texto
        )
