from __future__ import annotations

import pygame

from subjects import subject
from constants import blast_constants

# Uma classe para ditar quando um blast deverá ser spawnado
class BlastTimerSubject(subject.Subject):
    def __init__(self):
        subject.Subject.__init__(self)

        # Inicia o timer do blast
        self.event_type = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_type, blast_constants.BLAST_SPAWN_COOLDOWN)

        self.blast_speed = blast_constants.BLAST_BASE_SPEED

    def notify_all(self):
        # Cria o blast quando 
        for callback in self.observers:
            callback(self.blast_speed)

    def handle_events(self):
        # Pega apenas os eventos deste timer da fila do pygame
        blast_timer_events = pygame.event.get(self.event_type)

        # Notifica os inscritos caso o timer tenha apitado
        if len(blast_timer_events) > 0:
            for _ in range(len(blast_timer_events)):
                self.notify_all()
                self.blast_speed += blast_constants.SPEED_INCREMENT
