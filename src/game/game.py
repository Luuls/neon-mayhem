import pygame

from states.state import State
import states.menu_state as menu_state
import subjects.keyboard_subject as keyboard_subject

from utility.utils import get_assets_path

import game.game_constants as game_constants

from entities.blast import Blast
from entities.shield import Shield
from entities.player import Player

class Game():
    

    def __init__(self):
        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        pygame.display.set_caption('Neon Mayhem')
        
        # Inicia o timer do blast
        self.blast_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.blast_timer, 470)

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
        pygame.mixer.music.play()


        self.current_state: State = menu_state.MenuState(self)
        self.current_state.entering()

        self.keyboard_listener = keyboard_subject.KeyBoardSubject(
            self.current_state.update
        )

        # cria as entidades do jogo e inicializa o escudo
        self.player = Player()
        self.player.shield.update_shield_lane('UP')

        # inicia a lista do do blast
        self.blast_list = []


    def run(self):
        # Inicia o clock e define a taxa de frames
        clock = pygame.time.Clock()
        FPS = 60

        while True:
            self.keyboard_listener.handle_events()

            # if self.get_current_state() == 'LEVEL':
            #     if event.type == self.blast_timer:
            #         self.spawn_blast()
                    
            # Controle do que é exibido na tela no estado atual
            self.render_screen()
            clock.tick(FPS)
        
        
    def get_current_state(self) -> str:
        return self.current_state

    def set_state(self, new_state: State) -> None:
        self.current_state.exiting()
        self.keyboard_listener.unsubscribe(self.current_state.update)
        self.current_state = new_state
        self.keyboard_listener.subscribe(new_state.update)
        self.current_state.entering()
        
    def render_screen(self) -> None:
        self.current_state.render()
        pygame.display.flip()
    
    def spawn_blast(self):
        new_blast = Blast('Blue', 10)
        self.blast_list.append(new_blast)