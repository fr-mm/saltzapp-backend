# SaltZapp backend

API REST para chat

## Rotas 

### /api_v1/login/
#### POST {username, password}
Retorna um token de autorização para o respectivo usuário se os dados constarem no 
banco de dados (status 200) ou status 400 caso os dados sejam inválidos.

### /api_v1/mensagens/
#### POST {origem_id, destino_id, texto}
Cria uma mensagem de um usuário para outro (status 201) ou retorna status 400 caso dados inválidos.

### /api_v1/usuarios/
#### POST {username, password}
Cria um usuário quando os dados forem válidos (status 201) ou retorna status 400 caso inválidos.

### /api_v1/usuarios/{usuario_id}
#### GET
Retorna a última interação do usuário com cada um dos outros usuários ordenadas por data.

### /api_v1/usuarios/{usuario_id}/{outro_usuário_id}
#### GET
Retorna todas as mensagens trocadas entre os dois usuários.

### /api_v1/clientes/
#### POST {nome, whatsapp, divida}
Cria um novo cliente (status 201) ou retorna status 400 quando dados inválidos.

## Dependências
- [Docker](https://www.docker.com/): a única dependência real, irá gerenciar todas as outras
- [Django 4.1.5](https://www.djangoproject.com/): framework web 
- [Djongo 1.3.6](https://pypi.org/project/djongo/): driver para usar MongoDB no Django
- [Pymongo 3.12.3](https://pypi.org/project/pymongo/): usado pelo Djongo, necessita de um downgrade para fucionar com as versões acima citadas
- [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/): para criação de API REST
- [Django Cors Headers 3.13.0](https://pypi.org/project/django-cors-headers/): para gerencias headers necessários para Cross-Origin Resource Sharing (CORS)
- [Pytest 7.2.1](https://docs.pytest.org/en/7.2.x/): framework para testes
- [Pytest Django 4.5.2](https://pypi.org/project/pytest-django/): plugin para usar Pytest com Django 
- [FactoryBoy 3.2.1](https://factoryboy.readthedocs.io/en/stable/): para criação de fábricas de teste

## Uso
Na raiz do projeto, rode os containers:
```
sudo docker compose up
```
O servidor já estará disponível na porta 8000 do localhost
