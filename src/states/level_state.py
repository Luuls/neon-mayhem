from __future__ import annotations

import states.state as state
import states.menu_state as menu_state

import game.game as game
from utility import blast_spawner
import entities.player as player
import entities.blast as blast

from subjects import blast_timer_subject

import pygame
import sys

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)
        
        self.player = player.Player()
        
        self.blast_list: list[blast.Blast] = []
        self.blast_spawner = blast_spawner.BlastSpawner(self.blast_list)
        self.blast_timer_listener = blast_timer_subject.BlastTimerSubject()

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

    def exiting(self):
        self.game.keyboard_listener.unsubscribe(self.player.update)
        self.blast_timer_listener.unsubscribe(self.blast_spawner.spawn)

    def render(self):
        self.game.screen.blit(self.game.level_surface, (0, 0))
        
        self.game.screen.blit(self.player.shield.sprite, self.player.shield.rect)

        self.player.draw_at(self.game.screen)
        self.player.shield.draw_at(self.game.screen)
        for blast in self.blast_list:
            blast.draw_at(self.game.screen)

    def update(self, keys_pressed: list[int]):
        self.blast_timer_listener.handle_events()

        for i, blast in enumerate(self.blast_list):
            blast.update()

            if blast.rect.colliderect(self.player.rect):
                del self.blast_list[i]
                self.player.damage()
                
            elif blast.rect.colliderect(self.player.shield.rect):
                del self.blast_list[i]
                
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_m:
                self.game.set_state(menu_state.MenuState(self.game))
