from __future__ import annotations
from typing import Callable

from abc import ABC, abstractmethod

class Subject(ABC):
    # Callable é um tipo de objeto que pode ser chamado,
    # isto é, uma função
    def __init__(self):
        # Lista de funções que estão observando determinado assunto (subject)
        self.observers: list[Callable] = []

    # Inscreve na lista uma função para ser chamada
    # (inscreveremos na lista funções como State.update, etc. Depende do subject)
    def subscribe(self, observer_callback: Callable):
        self.observers.append(observer_callback)

    def unsubscribe(self, observer_callback: Callable):
        self.observers.remove(observer_callback)

    # Chamado a cada frame
    @abstractmethod
    def handle_events(self):
        pass

    # Método para notificar todas as funções da lista observers
    @abstractmethod
    def notify_all(self):
        pass
