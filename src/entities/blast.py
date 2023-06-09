from pygame import Surface, image, transform
import random

from utility.utils import get_assets_path
import game.game_constants as game_constants

# Classe dos projéteis
class Blast():

    def __init__(self, color, speed: int):

        assets_path = get_assets_path(__file__)
        self.blast_sprite = image.load(f'{assets_path}/sprites/blast_sprite.png').convert_alpha()
        
        self.color = color
        self.speed = speed

        # Designamos um caminho (lane) aleatório ao blast
        self.lane = random.randint(1, 4)

        if self.lane == 1:
            position_x = game_constants.SCREEN_WIDTH / 2
            position_y = 0
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 0, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))

        elif self.lane == 2:
            position_x = game_constants.SCREEN_WIDTH
            position_y = game_constants.SCREEN_HEIGHT / 2
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 90, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))

        elif self.lane == 3:
            position_x = game_constants.SCREEN_WIDTH / 2
            position_y = game_constants.SCREEN_HEIGHT
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 0, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))
        
        elif self.lane == 4:
            position_x = 0
            position_y = game_constants.SCREEN_HEIGHT / 2
            self.blast_sprite = transform.rotozoom(self.blast_sprite, 90, 0.05)
            self.blast_rect = self.blast_sprite.get_rect(center=(position_x, position_y))
        
    def update_position(self):

        # Os que vêm de cima/baixo devem ser mais lentos, pois isso
        # compensa pela sua proximidade em relação ao player.
        if self.lane == 1:
            self.blast_rect.y += self.speed / 1.75
    
        elif self.lane == 2:
            self.blast_rect.x -= self.speed
        
        elif self.lane == 3:
            self.blast_rect.y -= self.speed / 1.75
        
        elif self.lane == 4:
            self.blast_rect.x += self.speed

    def draw_at(self, screen: Surface):
        screen.blit(self.blast_sprite, self.blast_rect)