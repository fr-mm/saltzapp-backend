from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.otds import NovoUsuarioOTD, UsuarioOTD
from chat.repositorios import UsuarioRepositorio
from chat.serializers import NovoUsuarioOTDSerializer, UsuarioOTDSerializer


class UsuariosView(APIView):
    def post(self, request: Request) -> Response:
        try:
            novo_usuario_otd_serializer = NovoUsuarioOTDSerializer(data=request.data)
            novo_usuario_otd_serializer.is_valid(raise_exception=True)
            otd = NovoUsuarioOTD(**novo_usuario_otd_serializer.validated_data)
            usuario = UsuarioRepositorio.criar(otd.nome, otd.senha)
            token, created = Token.objects.get_or_create(user=usuario)
            usuario_otd = UsuarioOTD.de_modelo(usuario, token.key)
            usuario_serializer = UsuarioOTDSerializer(usuario_otd)

            return Response(
                status=201,
                data=usuario_serializer.data
            )

        except ValidationError:
            mensagem = 'Usuário ou senha inválidos'
            try:
                nome = request.data['nome']
                senha = request.data['senha']
                limites = NovoUsuarioOTDSerializer.limites()
                if len(nome) < limites.nome.tamanho_minimo:
                    mensagem = f'Nome deve ter no mínimo {limites.nome.tamanho_minimo} caracteres. '
                elif len(nome) > limites.nome.tamanho_maximo:
                    mensagem = f'Nome deve ter no máximo {limites.nome.tamanho_maximo} caracteres. '
                if len(senha) < limites.senha.tamanho_minimo:
                    mensagem += f'Senha deve ter no mínimo {limites.senha.tamanho_minimo} caracteres.'
                elif len(senha) > limites.senha.tamanho_maximo:
                    mensagem += f'Senha deve ter no máximo {limites.senha.tamanho_maximo} caracteres.'
            except KeyError:
                pass
            return Response(
                data=mensagem,
                status=400
            )
