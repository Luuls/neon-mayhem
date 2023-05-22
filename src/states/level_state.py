from __future__ import annotations

import states.state as state
import states.menu_state as menu_state

import game.game as game

import pygame
import sys

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)

    def entering(self):
        print(f'ENTERING {self.__class__.__name__}')

    def exiting(self):
        print(f'EXITING {self.__class__.__name__}')

    def render(self):
        self.game.screen.blit(self.game.level_surface, (0, 0))
        
        self.game.screen.blit(self.game.player.shield.shield_sprite, self.game.player.shield.shield_rect)
        self.game.player.draw_at(self.game.screen)

        eliminated = []
                
        for i in range(len(self.game.blast_list)):
            self.game.blast_list[i].draw_at(self.game.screen)
            self.game.blast_list[i].update_position()

            if self.game.blast_list[i].blast_rect.colliderect(self.game.player.rect):
                print('Você foi atingido!')
                eliminated.append(self.game.blast_list[i])
                    
            elif self.game.blast_list[i].blast_rect.colliderect(self.game.player.shield.shield_rect):
                eliminated.append(self.game.blast_list[i])

        self.game.blast_list = [x for x in self.game.blast_list if x not in eliminated]

    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_m:
                self.game.set_state(menu_state.MenuState(self.game))
            
            elif key == pygame.K_UP:
                self.game.player.shield.update_shield_lane('UP')
                
            elif key == pygame.K_DOWN:
                self.game.player.shield.update_shield_lane('DOWN')
                
            elif key == pygame.K_LEFT:
                self.game.player.shield.update_shield_lane('LEFT')
                

            elif key == pygame.K_RIGHT:
                self.game.player.shield.update_shield_lane('RIGHT')