from chat.models import ClienteEmCriacao, Usuario, Cliente


class ClienteEmCriacaoRepositorio:
    @classmethod
    def criar(cls, criador: Usuario, nome: str = None, whatsapp: str = None, divida: float = None) -> ClienteEmCriacao:
        return ClienteEmCriacao.objects.create(
            criador=criador,
            nome=nome,
            whatsapp=whatsapp,
            divida=divida
        )

    @classmethod
    def editar(
            cls,
            criador: Usuario,
            nome: str = None,
            whatsapp: str = None,
            divida: float = None
    ) -> ClienteEmCriacao:
        cliente_em_criacao: ClienteEmCriacao = ClienteEmCriacao.objects.get(criador=criador)
        if nome:
            cliente_em_criacao.nome = nome
        if whatsapp:
            cliente_em_criacao.whatsapp = whatsapp
        if divida is not None:
            cliente_em_criacao.divida = divida
        cliente_em_criacao.save()
        return cliente_em_criacao

    @classmethod
    def transformar_em_cliente(cls, cliente_em_criacao: ClienteEmCriacao) -> Cliente:
        cliente = Cliente.objects.create(
            nome=cliente_em_criacao.nome,
            whatsapp=cliente_em_criacao.whatsapp,
            divida=cliente_em_criacao.divida
        )
        cliente.save()
        cliente_em_criacao.delete()
        return cliente

    @classmethod
    def deletar_por_criador(cls, criador: Usuario) -> None:
        ClienteEmCriacao.objects.filter(criador=criador).delete()
