import factory

from chat.models import Usuario


class FabricaTesteUsuario(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    username = factory.Faker('name')
    password = factory.Faker('pystr', min_chars=6, max_chars=50)
