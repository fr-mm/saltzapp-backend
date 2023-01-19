from datetime import datetime

import factory

from chat.models import Mensagem
from testes.fabricas import FabricaTesteUsuario


class FabricaTesteMensagem(factory.django.DjangoModelFactory):
    class Meta:
        model = Mensagem

    enviada_em = factory.Faker('date_time', end_datetime=datetime.now())
    origem = factory.SubFactory(FabricaTesteUsuario)
    destino = factory.SubFactory(FabricaTesteUsuario)
    texto = factory.Faker('sentence')
