from __future__ import annotations

import states.state as state
import states.menu_state as menu_state

import game.game as game

class LevelState(state.State):
    def __init__(self, game_ref: game.Game):
        state.State.__init__(self, game_ref)

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
