from __future__ import annotations

import pygame

from subjects import subject

class BlastTimerSubject(subject.Subject):
    def __init__(self):
        subject.Subject.__init__(self)

        # Inicia o timer do blast
        self.BLAST_TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(self.BLAST_TIMER, 470)

        self.accepted_events: list[pygame.event.Event] = [self.BLAST_TIMER]
        pygame.event.set_allowed(self.accepted_events)

    def notify_all(self):
        for callback in self.observers:
            callback()

    def handle_events(self):
        blast_timer_events = pygame.event.get(self.accepted_events)
        if len(blast_timer_events) > 0:
            print('BLAST SPAWNED')
            self.notify_all()
