from __future__ import annotations

from abc import ABC, abstractmethod
import game.game as game

class State(ABC):
    def __init__(self, game_ref: game.Game) -> None:
        self.game = game_ref

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def update(self, event) -> None:
        pass

    @abstractmethod
    def entering(self) -> None:
        pass

    @abstractmethod
    def exiting(self) -> None:
        pass