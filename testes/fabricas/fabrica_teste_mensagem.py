from datetime import datetime

import factory

from chat.models import Mensagem


class FabricaTesteMensagem(factory.django.DjangoModelFactory):
    class Meta:
        model = Mensagem

    enviada_em = factory.Faker('date_time', end_datetime=datetime.now())
    origem_id = factory.Faker('uuid4')
    destino_id = factory.Faker('uuid4')
    texto = factory.Faker('sentence')
