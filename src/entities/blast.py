from pygame import Surface, image, transform
import random

from utility.utils import get_assets_path
import constants.game_constants as game_constants

# Classe dos projéteis
class Blast():

    def __init__(self, speed: int):

        assets_path = get_assets_path(__file__)
        self.blast_sprite = image.load(f'{assets_path}/sprites/blast_sprite.png').convert_alpha()
        
        self.speed = speed
        self.lane = random.choice(['UP', 'RIGHT', 'DOWN', 'LEFT'])

        if self.lane == 'UP':
            position_x = game_constants.SCREEN_WIDTH / 2
            position_y = 0
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 0, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))

        elif self.lane == 'RIGHT':
            position_x = game_constants.SCREEN_WIDTH
            position_y = game_constants.SCREEN_HEIGHT / 2
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 90, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))

        elif self.lane == 'DOWN':
            position_x = game_constants.SCREEN_WIDTH / 2
            position_y = game_constants.SCREEN_HEIGHT
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 0, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))
        
        elif self.lane == 'LEFT':
            position_x = 0
            position_y = game_constants.SCREEN_HEIGHT / 2
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 90, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))
        
    def update(self):

        if self.lane == 'UP':
            self.blast_rect.y += self.speed
    
        elif self.lane == 'RIGHT':
            self.blast_rect.x -= self.speed
        
        elif self.lane == 'DOWN':
            self.blast_rect.y -= self.speed
        
        elif self.lane == 'LEFT':
            self.blast_rect.x += self.speed

    def draw_at(self, screen: Surface):
        screen.blit(self.blast_sprite, self.blast_rect)