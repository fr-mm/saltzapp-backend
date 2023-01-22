from dataclasses import dataclass
from typing import List

from chat.otds.ultima_mensagem_otd import UltimaMensagemOTD
from chat.otds.mensagem_otd import MensagemOTD


@dataclass
class ConversaOTD:
    mensagens: List[MensagemOTD]
    ultimas_mensagens: List[UltimaMensagemOTD]
