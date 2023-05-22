from __future__ import annotations

import states.state as state
import states.level_state as level_state
import game.game as game

import pygame
import sys

class MenuState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)

    def entering(self):
        print(f'ENTERING {self.__class__.__name__}')

    def exiting(self):
        print(f'EXITING {self.__class__.__name__}')
        pygame.mixer.music.stop()

    def render(self):
        self.game.screen.blit(self.game.menu_surface, (0, 0))

        self.game.screen.blit(self.game.title_surface, self.game.title_rect)
        self.game.screen.blit(self.game.subtitle_surface, self.game.subtitle_rect)
        self.game.screen.blit(self.game.copyright_surface, self.game.copyright_rect)
    
    def update(self, keys_pressed: list[int]):
        print(keys_pressed)
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(level_state.LevelState(self.game))

    def handle_input(self):
        pass