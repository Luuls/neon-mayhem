from __future__ import annotations

from entities import blast
from game import game


class BlastSpawner():
    def __init__(self, game_ref: game.Game):
        self.game = game_ref

    def spawn(self) -> blast.Blast:
        self.game.blast_list.append(blast.Blast(10))        