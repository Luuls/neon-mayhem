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
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = 0
    
        elif self.lane == 2:
            self.position_x = game_constants.SCREEN_WIDTH
            self.position_y = game_constants.SCREEN_HEIGHT / 2
        
        elif self.lane == 3:
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = game_constants.SCREEN_HEIGHT
        
        elif self.lane == 4:
            self.position_x = 0
            self.position_y = game_constants.SCREEN_HEIGHT / 2
        
    def update_position(self):

        if self.lane == 1:
            self.position_y += self.speed
    
        elif self.lane == 2:
            self.position_x -= self.speed
        
        elif self.lane == 3:
            self.position_y -= self.speed
        
        elif self.lane == 4:
            self.position_x += self.speed

    def draw_at(self, screen: Surface):
        draw.circle(screen, self.color, (self.position_x, self.position_y), 20)