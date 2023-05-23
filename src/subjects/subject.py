from __future__ import annotations
from typing import Callable

from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.observers: list[Callable] = []

    # inscreve na lista uma função para ser chamada
    # (inscreveremos na lista funções como State.update, etc. Depende do subject)
    def subscribe(self, observer_callback: tuple[Callable]):
        self.observers.append(observer_callback)
        print(self.observers)

    def unsubscribe(self, observer_callback: Callable):
        self.observers.remove(observer_callback)

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def notify_all(self):
        pass