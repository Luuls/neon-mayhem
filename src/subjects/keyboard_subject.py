from __future__ import annotations
from typing import Callable

import subjects.subject as subject

import pygame

class KeyBoardSubject(subject.Subject):
    # Callable é um tipo de objeto que pode ser chamado.
    # isto é: uma função
    def __init__(self, observer_callback: Callable):
        self.keys_pressed = None
        self.accepted_events: list[pygame.event.Event] = [pygame.KEYDOWN]
        self.observers: list[Callable] = []
        print(observer_callback)
        self.subscribe(observer_callback)
        
    def subscribe(self, observer_callback: tuple[Callable]):
        self.observers.append(observer_callback)
        print(self.observers)

    def unsubscribe(self, observer_callback: Callable):
        self.observers.remove(observer_callback)

    def notify_all(self):
        for callback in self.observers:
            callback(self.keys_pressed)

    def handle_events(self):
        self.keys_pressed = pygame.event.get(self.accepted_events)
        if len(self.keys_pressed) > 0:
            self.notify_all()