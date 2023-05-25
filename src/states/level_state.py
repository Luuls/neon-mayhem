from __future__ import annotations

import states.state as state
import states.menu_state as menu_state

import game.game as game
from utility import blast_spawner
import entities.player as player

from subjects import blast_timer_subject

import pygame
import sys

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)

    def entering(self):
        print(f'ENTERING {self.__class__.__name__}')
        self.player = player.Player()
        self.player.shield.move_shield('UP')

        self.game.keyboard_listener.subscribe(self.player.update)
        pygame.event.set_blocked(None)
        self.blast_spawner = blast_spawner.BlastSpawner(self.game)
        self.blast_timer_listener = blast_timer_subject.BlastTimerSubject()
        self.blast_timer_listener.subscribe(self.blast_spawner.spawn)
        pygame.event.set_allowed(
            [
                self.game.keyboard_listener.event_type,
                self.blast_timer_listener.event_type
            ]
        )

    def exiting(self):
        print(f'EXITING {self.__class__.__name__}')
        self.game.keyboard_listener.unsubscribe(self.player.update)
        self.blast_timer_listener.unsubscribe(self.blast_spawner.spawn)

        pygame.event.set_blocked(None)

    def render(self):
        self.game.screen.blit(self.game.level_surface, (0, 0))
        
        self.game.screen.blit(self.player.shield.sprite, self.player.shield.rect)
        self.player.draw_at(self.game.screen)
        self.player.shield.draw_at(self.game.screen)

        eliminated = []
                
        for i in range(len(self.game.blast_list)):
            self.game.blast_list[i].draw_at(self.game.screen)
            self.game.blast_list[i].update()

            # if self.game.blast_list[i].blast_rect.colliderect(self.game.player.rect):
            #     print('Você foi atingido!')
            #     eliminated.append(self.game.blast_list[i])
                    
            # elif self.game.blast_list[i].blast_rect.colliderect(self.game.player.shield.shield_rect):
            #     eliminated.append(self.game.blast_list[i])

        # self.game.blast_list = [x for x in self.game.blast_list if x not in eliminated]

    def update(self, keys_pressed: list[int]):
        self.blast_timer_listener.handle_events()

        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_m:
                self.game.set_state(menu_state.MenuState(self.game))
            