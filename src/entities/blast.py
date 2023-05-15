from pygame import draw, Surface
import random

import game.game_constants as game_constants

# Classe dos projéteis
class Blast:
    def __init__(self, color, speed: int):
        self.color = color
        self.speed = speed
        self.lane = random.randint(1, 4)

        if self.lane == 1:
            # lado de cima da tela
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = 0
    
        elif self.lane == 2:
            # lado direito da tela
            self.position_x = game_constants.SCREEN_WIDTH
            self.position_y = game_constants.SCREEN_HEIGHT / 2
            # velocidade deve ser oposta, pois o blast precisa ir para a esquerda
            self.speed *= -1
        
        elif self.lane == 3:
            # lado de baixo da tela
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = game_constants.SCREEN_HEIGHT
            # velocidade deve ser oposta, pois o blast precisa subir
            self.speed *= -1
        
        elif self.lane == 4:
            # lado esquedo da tela
            self.position_x = 0
            self.position_y = game_constants.SCREEN_HEIGHT / 2
        
    def update_position(self):
        # pela convenção adotada, o blast se move em x se a lane for par
        # e em y se a lane for ímpar
        if self.lane % 2 == 0:
            self.position_x += self.speed

        else:
            self.position_y += self.speed 

    def draw_at(self, screen: Surface):
        draw.circle(screen, self.color, (self.position_x, self.position_y), 20)