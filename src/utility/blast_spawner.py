from __future__ import annotations

from entities import blast

class BlastSpawner:
    def __init__(self, blast_list_ref: list[blast.Blast]):
        self.blast_list_ref = blast_list_ref

    def spawn(self, speed: float ) -> None:
        self.blast_list_ref.append(blast.Blast(speed))        
