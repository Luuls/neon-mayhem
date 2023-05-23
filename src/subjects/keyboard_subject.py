from __future__ import annotations

import subjects.subject as subject

import pygame

class KeyBoardSubject(subject.Subject):
    # Callable é um tipo de objeto que pode ser chamado.
    # isto é: uma função
    def __init__(self):
        subject.Subject.__init__(self)

        self.keys_pressed = None
        self.accepted_events: list[pygame.event.Event] = [pygame.KEYDOWN]
        pygame.event.set_allowed(self.accepted_events)
        
    def handle_events(self):
        self.keys_pressed = [event.key for event in pygame.event.get(self.accepted_events)]
        if len(self.keys_pressed) > 0:
            print(self.keys_pressed)
            self.notify_all()

    def notify_all(self):
        for callback in self.observers:
            callback(self.keys_pressed)
