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
        self.game.screen.blit(self.game.menu_surface, (0, 0))

        self.game.screen.blit(self.game.title_surface, self.game.title_rect)
        self.game.screen.blit(self.game.subtitle_surface, self.game.subtitle_rect)
        self.game.screen.blit(self.game.copyright_surface, self.game.copyright_rect)
    
    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(level_state.LevelState(self.game))
