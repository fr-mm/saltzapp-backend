import factory

from chat.models import Mensagem
from testes.fabricas import FabricaTesteUsuario


class FabricaTesteMensagem(factory.django.DjangoModelFactory):
    class Meta:
        model = Mensagem

    origem = factory.SubFactory(FabricaTesteUsuario)
    destino = factory.SubFactory(FabricaTesteUsuario)
    texto = factory.Faker('sentence')
