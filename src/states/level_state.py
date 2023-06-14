from __future__ import annotations

import states.state as state
import states.menu_state as menu_state
import states.game_over_state as game_over_state

import game.game as game
from utility.blast_spawner import BlastSpawner
from entities.player import Player
from entities.blast import Blast

from subjects import blast_timer_subject

import pygame
import sys

from utility.utils import get_assets_path

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)
        
        self.player = Player()
        
        self.blast_list: list[Blast] = []
        self.blast_spawner = BlastSpawner(self.blast_list)
        self.blast_timer_listener = blast_timer_subject.BlastTimerSubject()

        assets_path = get_assets_path(__file__)
        
        # Inicializa os efeitos sonoros
        self.shield_impact_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/shield_impact.wav')
        self.shield_impact_sound.set_volume(0.10)
        self.damage_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/damage.wav')
        self.press_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/press.wav')

        self.ui_font = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 25)
        self.lives_surface: pygame.Surface
        self.score_surface: pygame.Surface
        
        self.lives_rect: pygame.Rect
        
        pygame.mixer.music.load(f'{assets_path}/songs/level_track.mp3')

    def entering(self):
        self.game.keyboard_listener.subscribe(self.player.update)
        self.blast_timer_listener.subscribe(self.blast_spawner.spawn)

        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
                self.game.keyboard_listener.event_type,
                self.blast_timer_listener.event_type
            ]
        )

        # reproduz a música do jogo em loop
        pygame.mixer.music.play()

    def exiting(self):
        self.game.keyboard_listener.unsubscribe(self.player.update)
        self.blast_timer_listener.unsubscribe(self.blast_spawner.spawn)
        
    def update(self, keys_pressed: list[int]):
        self.blast_timer_listener.handle_events()

        for i, blast in enumerate(self.blast_list):
            blast.update()

            if blast.rect.colliderect(self.player.rect):
                del self.blast_list[i]

                self.player.damage()
                self.damage_sound.play()

                if not self.player.is_alive:
                    self.game.set_state(game_over_state.GameOverState(self.game))

            elif blast.rect.colliderect(self.player.shield.rect):
                del self.blast_list[i]

                self.shield_impact_sound.play()

        self.lives_surface = self.ui_font.render(
            f'Lives: {self.player.health}', True, 'White'
        )
        self.lives_rect = self.lives_surface.get_rect(
            bottomleft=(40, 702)
        )

        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_m:
                self.game.set_state(menu_state.MenuState(self.game))

    def render(self):
        self.game.screen.blit(self.game.level_surface, (0, 0))
        self.game.screen.blit(self.lives_surface, self.lives_rect)
        
        self.game.screen.blit(self.player.shield.sprite, self.player.shield.rect)

        self.player.draw_at(self.game.screen)
        self.player.shield.draw_at(self.game.screen)
        for blast in self.blast_list:
            blast.draw_at(self.game.screen)

