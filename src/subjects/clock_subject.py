from __future__ import annotations
from typing import Callable

import subjects.subject as subject

import pygame

class KeyBoardListener(subject.Subject):
    def __init__(self, *observers_callbacks: tuple[Callable]):
        self.keys_pressed = None
        self.accepted_events: list[int] = [pygame.KEYDOWN]
        self.observers: list[Callable] = []
        self.subscribe(observers_callbacks)
        
    def subscribe(self, *observers_callbacks: tuple[Callable]):
        self.observers += observers_callbacks

    def unsubscribe(self, observer_callback: Callable):
        self.observers.remove(observer_callback)

    def notify_all(self):
        for callback in self.observers:
            callback(self.keys_pressed)

    def handle_events(self):
        self.keys_pressed = pygame.event.get(self.accepted_events)
        self.notify_all()