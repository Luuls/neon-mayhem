from __future__ import annotations

import pygame

from subjects import subject

class BlastTimerSubject(subject.Subject):
    def __init__(self):
        subject.Subject.__init__(self)

        # Inicia o timer do blast
        self.event_type = pygame.USEREVENT + 1
        pygame.time.set_timer(self.event_type, 470)

    def notify_all(self):
        for callback in self.observers:
            callback()

    def handle_events(self):
        blast_timer_events = pygame.event.get(self.event_type)
        if len(blast_timer_events) > 0:
            for _ in range(len(blast_timer_events)):
                self.notify_all()
                print('BLAST SPAWNED')
