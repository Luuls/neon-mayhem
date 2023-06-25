from __future__ import annotations

import pygame
import sys

import states.state as state
import states.level_state as level_state
import game.game as game

from constants import game_constants
from constants import menu_constants

from utility.utils import get_assets_path

class MenuState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)
        
        assets_path = get_assets_path(__file__)
        
        # CARREGAMENTO DOS ASSETS DO MENU
        background_load = pygame.image.load(f'{assets_path}/backgrounds/menu_background.jpg')
        self.background_surface = pygame.transform.scale(
            background_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        self.game_title_surface = pygame.image.load(f'{assets_path}/icon/game_logo.png')
        self.game_title_surface = pygame.transform.scale_by(
            self.game_title_surface, 1.5
        )
        self.game_title_rect = self.game_title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 200)
        )
        

        self.copyright = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 17)
        self.copyright_surface = self.copyright.render(
            '2023 Nemesis Game Co. Published by M. R. Zatelli. All rights reserved.', True, 'White'
        )
        self.copyright_rect = self.copyright_surface.get_rect(
            bottomleft=(20, 702)
        )
        
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)
        # FIM DO CARREGAMENTO DOS ASSETS DO MENU

    def entering(self):
        # Permite que o pygame leia apenas o teclado
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [self.game.keyboard_listener.event_type]
        )
        
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_pos(menu_constants.MUSIC_DROP_TIMESTAMP)
            
    def exiting(self):
        pygame.mixer.music.stop()

    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(level_state.LevelState(self.game))
                
    def render(self):
        self.game.screen.blit(self.background_surface, (0, 0))

        self.game.screen.blit(self.game_title_surface, self.game_title_rect)

        self.game.screen.blit(self.copyright_surface, self.copyright_rect)
