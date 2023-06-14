from __future__ import annotations

import pygame
import sys

import states.state as state
import states.menu_state as menu_state

import game.game as game
from utility.utils import get_assets_path
from constants import game_constants

class IntroState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)

        self.frame_counter = 0
        self.total_intro_frames: int = 40 * game_constants.FPS
        self.alpha_increment: float = 255 / self.total_intro_frames

        self.black_screen = pygame.Surface(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        self.black_screen.fill((0, 0, 0))
        
        self.black_screen_alpha: float = 255

        assets_path = get_assets_path(__file__)
        # Inicializa a fonte da animação no começo do jogo
        self.intro_credits = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.intro_credits_2 = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        
        self.intro_credits_surf = self.intro_credits.render(
            'NEMESIS GAME COMPANY', True, 'Grey'
        )
        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )
        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)

    def entering(self):
        pygame.mixer.music.play()
        pygame.event.set_allowed(self.game.keyboard_listener.event_type)
        # self.game.set_state(menu_state.MenuState(self.game))

    def exiting(self):
        print(self.black_screen_alpha)
        pass

    def update(self, keys_pressed: list[int]):
        if self.frame_counter == self.total_intro_frames:
            self.game.set_state(menu_state.MenuState(self.game))
        
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state(menu_state.MenuState(self.game))

        self.black_screen_alpha -= self.alpha_increment
        self.black_screen.set_alpha(int(self.black_screen_alpha))

        self.frame_counter += 1

    def render(self):
        self.game.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
        self.game.screen.blit(self.black_screen, (0, 0))

