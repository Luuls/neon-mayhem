from __future__ import annotations

import pygame
import sys

import states.state as state
import states.menu_state as menu_state
import states.game_over_state as game_over_state

import game.game as game
from utility import blast_spawner
from entities.player import Player
from entities.blast import Blast

from subjects import blast_timer_subject

from utility.utils import get_assets_path

from constants import game_constants

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)
        
        self.player = Player()
        
        # Lista para manter vista dos blasts ativos na tela
        self.blast_list: list[Blast] = []

        # spawnador de blasts
        self.blast_spawner = blast_spawner.BlastSpawner(self.blast_list)
        self.blast_timer_listener = blast_timer_subject.BlastTimerSubject()

        assets_path = get_assets_path(__file__)
        
        # CARREGAMENTO DOS ASSETS DO LEVEL
        background_load = pygame.image.load(f'{assets_path}/backgrounds/level_background.jpg').convert()
        self.background_surface = pygame.transform.scale(
            background_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        self.shield_impact_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/shield_impact.wav')
        self.shield_impact_sound.set_volume(0.10)
        self.damage_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/damage.wav')
        self.press_sound = pygame.mixer.Sound(f'{assets_path}/sound_effects/press.wav')

        self.ui_font = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 50)
        
        self.lives_surface = self.ui_font.render(
            f'Lives: {self.player.health}', True, 'White'
        )
        self.lives_rect = self.lives_surface.get_rect(
            bottomleft=(40, 702)
        )

        self.score_surface = self.ui_font.render(
            f'Score: {self.player.score}', True, 'White'
        )
        self.score_rect = self.score_surface.get_rect(
            bottomright=(game_constants.SCREEN_WIDTH - 40, 702)
        )

        self.score_multiplier_surface = self.ui_font.render(
            f'X{int(self.player.score_multiplier)}', True, 'White'
        )
        self.score_multiplier_rect = self.score_multiplier_surface.get_rect(
            bottomright=(game_constants.SCREEN_WIDTH - 40, 702 - 50)
        )

        pygame.mixer.music.load(f'{assets_path}/songs/level_track.mp3')
        # FIM DO CARREGAMENTO DOS ASSETS DO LEVEL

    def entering(self):
        # Inscreve métodos observadores a serem notificados (chamados)
        # Por exemplo: o método update do player vai ser chamado sempre
        # que alguma tecla for pressionada. 
        # Já o método spawn do blast spawner será chamado sempre que
        # o timer apitar.
        self.game.keyboard_listener.subscribe(self.player.update)
        self.blast_timer_listener.subscribe(self.blast_spawner.spawn)

        # Permite que o pygame leia apenas eventos de teclado e o evento de
        # timer
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [
                self.game.keyboard_listener.event_type,
                self.blast_timer_listener.event_type
            ]
        )

        # reproduz a música do jogo em loop
        pygame.mixer.music.play(-1)

    def exiting(self):
        # Ao sair do estado, desinscreve todos os métodos que foram inscritos
        self.game.keyboard_listener.unsubscribe(self.player.update)
        self.blast_timer_listener.unsubscribe(self.blast_spawner.spawn)
        
    def update(self, keys_pressed: list[int]):
        self.blast_timer_listener.handle_events()

        # Atualiza todos os blasts e verifica colisões
        for i, blast in enumerate(self.blast_list):
            blast.update()

            # Colisão de blast com o jogador
            if blast.rect.colliderect(self.player.rect):
                del self.blast_list[i]

                self.player.damage()
                self.damage_sound.play()

                if not self.player.is_alive:
                    self.game.set_state(
                        game_over_state.GameOverState(self.game, self.player.score)
                    )

            # Colisão de blast com o escudo
            elif blast.rect.colliderect(self.player.shield.rect):
                del self.blast_list[i]

                self.shield_impact_sound.play()
                self.player.score += int(self.player.score_multiplier)
                self.player.score_multiplier += 1 / game_constants.STEPS_TO_INCREMENT_MULTIPLIER
        
        self.score_surface = self.ui_font.render(
            f'Score: {self.player.score}', True, 'White'
        )
        self.score_rect = self.score_surface.get_rect(
            bottomright=(game_constants.SCREEN_WIDTH - 40, 702)
        )
        
        self.score_multiplier_surface = self.ui_font.render(
            f'X{int(self.player.score_multiplier)}', True, 'White'
        )
        self.score_multiplier_rect = self.score_multiplier_surface.get_rect(
            bottomright=(game_constants.SCREEN_WIDTH - 40, 702 - 50)
        )

        # Tratamento das teclas pressionadas no frame
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_m:
                self.game.set_state(menu_state.MenuState(self.game))

    def render(self):
        self.game.screen.blit(self.background_surface, (0, 0))
        self.game.screen.blit(self.score_surface, self.score_rect)
        self.game.screen.blit(self.score_multiplier_surface, self.score_multiplier_rect)
        
        self.game.screen.blit(self.player.shield.sprite, self.player.shield.rect)
        
        if self.player.health == 3:
            self.game.screen.blit(self.player.health_heart_3, self.player.health_heart_3_rect)
            self.player.draw_at(self.game.screen)

        elif self.player.health == 2:
            self.game.screen.blit(self.player.health_heart_2, self.player.health_heart_2_rect)
            self.player.draw_at(self.game.screen)

        elif self.player.health == 1:
            self.game.screen.blit(self.player.health_heart_1, self.player.health_heart_1_rect)
            self.player.draw_at(self.game.screen)

        self.player.draw_at(self.game.screen)
        self.player.shield.draw_at(self.game.screen)
        for blast in self.blast_list:
            blast.draw_at(self.game.screen)

