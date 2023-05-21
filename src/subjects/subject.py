from __future__ import annotations
from typing import Callable

from abc import ABC, abstractmethod

import pygame

class Subject(ABC):
    # inscreve na lista uma função para ser chamada
    # (inscreveremos na lista funções como State.update, etc. Depende do subject)

    @abstractmethod
    def subscribe(self, observer_callback: Callable):
        pass

    @abstractmethod
    def unsubscribe(self, observer_callback: Callable):
        pass

    @abstractmethod
    def notify_all(self):
        pass