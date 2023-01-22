from django.test import TestCase

from chat.models import ClienteEmCriacao, Cliente
from chat.repositorios.cliente_em_cliacao_repositorio import ClienteEmCriacaoRepositorio
from testes.fabricas import FabricaTesteUsuario


class TestClienteEmCriacaoRepositorio(TestCase):
    def test_criar_QUANDO_sem_argumentos_ENTAO_cria(self) -> None:
        usuario = FabricaTesteUsuario.create()

        ClienteEmCriacaoRepositorio.criar(criador=usuario)

        criado = ClienteEmCriacao.objects.all()[0]
        self.assertEqual(criado.criador, usuario)

    def test_editar_QUANDO_divida_informada_ENTAO_atualiza_divida(self) -> None:
        usuario = FabricaTesteUsuario.create()
        ClienteEmCriacao.objects.create(criador=usuario)
        divida = 10

        ClienteEmCriacaoRepositorio.editar(criador=usuario, divida=divida)

        cliente_em_criacao = ClienteEmCriacao.objects.get(criador=usuario)
        self.assertEqual(cliente_em_criacao.divida, divida)

    def test_transformar_em_cliente_QUANDO_cadastro_completo_ENTAO_cria_cliente(self) -> None:
        usuario = FabricaTesteUsuario.create()
        nome = 'Cliente em Criação'
        whatsapp = '5571988887777'
        divida = 1
        cliente_em_criacao = ClienteEmCriacao.objects.create(criador=usuario, nome=nome, whatsapp=whatsapp, divida=divida)

        ClienteEmCriacaoRepositorio.transformar_em_cliente(cliente_em_criacao)

        cliente = Cliente.objects.get(nome=nome)
        atributos = [cliente.whatsapp, cliente.divida]
        atributos_esperados = [whatsapp, divida]
        self.assertEqual(atributos, atributos_esperados)

    def test_transformar_em_cliente_QUANDO_cadastro_completo_ENTAO_deleta_cliente_em_criacao(self) -> None:
        usuario = FabricaTesteUsuario.create()
        nome = 'Cliente em Criação'
        whatsapp = '5571988887777'
        divida = 1
        cliente_em_criacao = ClienteEmCriacao.objects.create(criador=usuario, nome=nome, whatsapp=whatsapp, divida=divida)

        ClienteEmCriacaoRepositorio.transformar_em_cliente(cliente_em_criacao)

        with self.assertRaises(ClienteEmCriacao.DoesNotExist):
            ClienteEmCriacao.objects.get(criador=usuario)

    def test_transformar_em_cliente_QUANDO_apos_edicoes_ENTAO_cria_cliente(self) -> None:
        usuario = FabricaTesteUsuario.create()
        nome = 'Cliente em Criação'
        whatsapp = '5571988887777'
        divida = 1
        ClienteEmCriacao.objects.create(criador=usuario)
        ClienteEmCriacaoRepositorio.editar(criador=usuario, whatsapp=whatsapp)
        ClienteEmCriacaoRepositorio.editar(criador=usuario, nome=nome)
        cliente_em_criacao = ClienteEmCriacaoRepositorio.editar(criador=usuario, divida=divida)

        ClienteEmCriacaoRepositorio.transformar_em_cliente(cliente_em_criacao)

        cliente = Cliente.objects.get(nome=nome)
        atributos = [cliente.whatsapp, cliente.divida]
        atributos_esperados = [whatsapp, divida]
        self.assertEqual(atributos, atributos_esperados)
