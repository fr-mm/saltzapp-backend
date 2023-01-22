from chat.mensagens_de_bot.mensagem_com_substituicao import MensagemComSubstituicao
from chat.mensagens_de_bot.mensagem_de_whats import MensagemDeWhats
from chat.mensagens_de_bot.mensagem_simples import MensagemSimples
from chat.models import Cliente


intro = MensagemComSubstituicao(
    texto='Oi {nome}! Como posso ajudar? (digite 0 a qualquer momento para cancelar a operação)\n'
          '1 - cadastrar cliente\n'
          '2 - cobrar clientes',
    substituicao=MensagemComSubstituicao.substituir('{nome}', MensagemComSubstituicao.REGEX_REPLACE_NOME),
    comparar_primeiros_caracteres=3
)

pergunta_whats_do_cliente = MensagemSimples(
    'Qual o whatsapp do(a) cliente?'
)

pergunta_nome_do_cliente = MensagemSimples(
    'Qual o nome do(a) cliente?'
)

pergunta_divida_do_cliente = MensagemSimples(
    'Quanto ele(a) deve?'
)

cliente_cadastrado = MensagemComSubstituicao(
    texto='Cliente {nome} cadastrado com sucesso!',
    substituicao=MensagemComSubstituicao.substituir('{nome}', MensagemComSubstituicao.REGEX_REPLACE_NOME),
    comparar_primeiros_caracteres=8
)

whats_invalido = MensagemSimples(
    'Número de telefone inválido, favor informar no formato 5571988887777'
)

nome_invalido = MensagemSimples(
    f'Nome inválido ou já existente, informe outro ({Cliente.config().NOME_TAMANHO_MINIMO} '
    f'a {Cliente.config().NOME_TAMANHO_MAXIMO} caracteres)'
)

divida_invalida = MensagemSimples(
    f'Dívida inválida, favor informar no formato 123.45 (mínimo: {Cliente.config().DIVIDA_VALOR_MINIMO})'
)

cobrancas_enviadas = MensagemSimples(
    'Uma cobrança foi enviada para todos os clientes com dívidas'
)

atendimento_encerrado = MensagemSimples(
    'Atendimento encerrado'
)

cobranca_por_whats = MensagemDeWhats(
    'Olá {nome}, você tem uma dívida no valor de {divida}. Favor entrar em contato.'
)
