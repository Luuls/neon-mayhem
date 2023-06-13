from __future__ import annotations

import subjects.subject as subject

import pygame

class KeyBoardSubject(subject.Subject):
    def __init__(self):
        subject.Subject.__init__(self)

        self.keys_pressed: list[int] = []
        self.event_type = pygame.KEYDOWN
        
    def handle_events(self):
        self.keys_pressed = [event.key for event in pygame.event.get(self.event_type)]
        if len(self.keys_pressed) > 0:
            self.notify_all()

    def notify_all(self):
        for callback in self.observers:
            callback(self.keys_pressed)
