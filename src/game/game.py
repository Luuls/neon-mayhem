from __future__ import annotations

import pygame

from states.state import State
import states.intro_state as intro_state

import subjects.keyboard_subject as keyboard_subject

from utility.utils import get_assets_path

from constants import game_constants

class Game():
    def __init__(self):
        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Determina o caminho dos assets
        assets_path = get_assets_path(__file__)

        # Personaliza a janela do jogo
        pygame.display.set_caption('Neon Mayhem')
        self.icon_load = pygame.image.load(f'{assets_path}/icon/icon.jpg').convert()
        pygame.display.set_icon(self.icon_load)

        # não registra nenhum evento na fila de eventos.
        # possibilita que cada estado defina quais tipos
        # de eventos serão lidos pelo pygame
        pygame.event.set_blocked(None)
        
        self.keyboard_listener = keyboard_subject.KeyBoardSubject()

        self.current_state: State = intro_state.IntroState(self)
        self.current_state.entering()

    def run(self):
        # Inicia o clock
        clock = pygame.time.Clock()

        while True:
            self.keyboard_listener.handle_events()
            self.update(self.keyboard_listener.keys_pressed)
            self.render()
            clock.tick(game_constants.FPS)
        
    def set_state(self, new_state: State) -> None:
        self.current_state.exiting()
        self.current_state = new_state
        self.current_state.entering()
        
    def update(self, keys_pressed: list[int]):
        self.current_state.update(keys_pressed)
    
    def render(self) -> None:
        self.current_state.render()
        pygame.display.flip()
