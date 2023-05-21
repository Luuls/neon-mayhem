from __future__ import annotations

from abc import ABC, abstractmethod
import game.game as game

class State(ABC):
    def __init__(self, game_ref: game.Game) -> None:
        self.game = game_ref

    @abstractmethod
    def render(self) -> None:
        pass

    def update(self, event) -> None:
        pass

    @abstractmethod
    def handle_input(self) -> None:
        pass

    def entering(self) -> None:
        print(f'ENTERING {self.__class__.__name__} STATE')

    def exiting(self) -> None:
        print(f'EXITING {self.__class__.__name__} STATE')