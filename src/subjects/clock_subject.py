from __future__ import annotations
from typing import Callable

import subjects.subject as subject

class KeyBoardListener(subject.Subject):
    def __init__(self, *observers_callbacks: tuple[Callable]):
        self.observers = []
        self.subscribe(observers_callbacks)
        
    def subscribe(self, *observers_callbacks: tuple[Callable]):
        self.observers += observers_callbacks

    def unsubscribe(self, observer_callback: Callable):
        self.observers.remove(observer_callback)

    def notify_all(self):
        for callback in self.observers:
            callback(self.keys_pressed)
