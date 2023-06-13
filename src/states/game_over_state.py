from __future__ import annotations

import pygame
import sys

import states.state as state
import states.menu_state as menu_state
import states.level_state as level_state
import game.game as game

from utility.utils import get_assets_path
from constants import game_constants

class GameOverState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref) 
        
        assets_path = get_assets_path(__file__)
        
        background_load = pygame.image.load(f'{assets_path}/backgrounds/over_background.jpg')
        self.background_surface = pygame.transform.scale(
            background_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        # Inicializa o texto da tela de game over
        self.title = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.title_surface = self.title.render(
            'GAME OVER', True, '#01bfff'
        )
        self.title_rect = self.title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 - 20)
        )
        
        self.retry_surface = self.title.render(
            'PRESS ANY KEY TO CONTINUE', True, '#01bfff'
        )
        self.retry_rect = self.retry_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 + 55)
        )

    def entering(self):
        pass

    def exiting(self):
        pass

    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(menu_state.MenuState(self.game))

            elif key == pygame.K_SPACE:
                self.game.set_state(level_state.LevelState(self.game))

    def render(self):
        self.game.screen.blit(self.background_surface, (0, 0))

        self.game.screen.blit(self.title_surface, self.title_rect)
        self.game.screen.blit(self.retry_surface, self.retry_rect)
