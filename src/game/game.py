import pygame

from states.state import State
import states.menu_state as menu_state
import subjects.keyboard_subject as keyboard_subject

from utility.utils import get_assets_path

from constants import game_constants

from entities.blast import Blast

class Game():
    def __init__(self):
        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        pygame.display.set_caption('Neon Mayhem')
        
        assets_path = get_assets_path(__file__)
        # Inicializa as imagens do menu e do level
        menu_load = pygame.image.load(f'{assets_path}/backgrounds/menu_background.jpg').convert()
        self.menu_surface = pygame.transform.scale(
            menu_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        level_load = pygame.image.load(f'{assets_path}/backgrounds/level_background.jpg').convert()
        self.level_surface = pygame.transform.scale(
            level_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Inicializa o texto do menu
        self.title = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.title_surface = self.title.render(
            'NEON MAYHEM', True, '#01bfff'
        )
        self.title_rect = self.title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 50)
        )

        self.subtitle = self.title
        self.subtitle_surface = self.subtitle.render(
            'Press ENTER to play', True, '#01bfff'
        )
        self.subtitle_rect = self.subtitle_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 150)
        )

        self.copyright = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 17)
        self.copyright_surface = self.copyright.render(
            '2023 Nemesis Game Co. Published by M. R. Zatelli. All rights reserved.', True, 'White'
        )
        self.copyright_rect = self.copyright_surface.get_rect(
            bottomleft=(20, 702)
        )

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)

        # não registra nenhum evento na fila de eventos
        pygame.event.set_blocked(None)

        self.keyboard_listener = keyboard_subject.KeyBoardSubject()

        self.current_state: State = menu_state.MenuState(self)
        self.current_state.entering()

        # inicia a lista do do blast
        self.blast_list: list[Blast] = []

    def run(self):
        # Inicia o clock e define a taxa de frames
        clock = pygame.time.Clock()

        while True:
            self.keyboard_listener.handle_events()
            self.update(self.keyboard_listener.keys_pressed)
            self.render()
            clock.tick(game_constants.FPS)
        
        
    def get_current_state(self) -> str:
        return self.current_state

    def set_state(self, new_state: State) -> None:
        self.current_state.exiting()
        self.current_state = new_state
        self.current_state.entering()
        
    def update(self, keys_pressed: list[int]):
        self.current_state.update(keys_pressed)
    
    def render(self) -> None:
        self.current_state.render()
        pygame.display.flip()