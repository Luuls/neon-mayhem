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
        
        assets_path = get_assets_path(__file__)
        
        self.press_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/press.wav')
        
        self.fade = pygame.Surface((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.fade.fill((0, 0, 0))
        
        # Inicializa a fonte da animação no começo do jogo
        self.intro_credits = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.intro_credits_2 = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        
        self.intro_credits_surface = self.intro_credits.render(
            'NEMESIS GAME COMPANY', True, 'Grey'
        )
        self.intro_credits_rect = self.intro_credits_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )
        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)

    def entering(self):
        pygame.mixer.music.play()
        pygame.event.set_allowed(self.game.keyboard_listener.event_type)

    def exiting(self):
        pass

    # muito trabalho resolver esse negócio eu só copiei e colei 
    def update(self, keys_pressed: list[int]):
        self.intro_credits_surface = self.intro_credits.render(
            'NEMESIS GAME COMPANY', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )

        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return
            
            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return
            
            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        self.intro_credits_surface = self.intro_credits.render(
            'IN ASSOCIATION WITH', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 280)
        )

        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return
            
            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        self.intro_credits_2_surf = self.intro_credits_2.render(
            'M. R. Zatelli and UFSC', True, 'Grey'
        )

        self.intro_credits_2_rect = self.intro_credits_2_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 390)
        )

        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return

            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.intro_credits_2_surf, self.intro_credits_2_rect)
            self.game.screen.blit(self.fade, (0, 300))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return

            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.intro_credits_2_surf, self.intro_credits_2_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)

        self.intro_credits_surface = self.intro_credits.render(
            'PRESENT', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )

        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return

            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    self.game.set_state(menu_state.MenuState(self.game))
                    return

            self.fade.set_alpha(alpha)
            self.game.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)

        self.game.set_state(menu_state.MenuState(self.game))

    def render(self):
        self.game.screen.blit(self.intro_credits_surface, self.intro_credits_rect)

