from __future__ import annotations

import pygame
import sys

import states.state as state
import states.level_state as level_state
import game.game as game

from constants import game_constants
from utility.utils import get_assets_path

class MenuState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)
        
        assets_path = get_assets_path(__file__)
        
        background_load = pygame.image.load(f'{assets_path}/backgrounds/menu_background.jpg')
        self.background_surface = pygame.transform.scale(
            background_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
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


    def entering(self):
        self.game.keyboard_listener.subscribe(self.update)

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [self.game.keyboard_listener.event_type]
        )
        
        pygame.mixer.music.play()

    def exiting(self):
        self.game.keyboard_listener.unsubscribe(self.update)

        pygame.mixer.music.stop()

    def render(self):
        self.game.screen.blit(self.background_surface, (0, 0))

        self.game.screen.blit(self.title_surface, self.title_rect)
        self.game.screen.blit(self.subtitle_surface, self.subtitle_rect)
        self.game.screen.blit(self.copyright_surface, self.copyright_rect)
    
    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(level_state.LevelState(self.game))
