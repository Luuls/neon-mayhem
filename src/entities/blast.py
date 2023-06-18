from __future__ import annotations

import pygame
import random

from utility.utils import get_assets_path
import constants.game_constants as game_constants

# Classe dos projéteis
class Blast():
    def __init__(self, speed: float):
        assets_path = get_assets_path(__file__)
        
        self.sprite = pygame.image.load(f'{assets_path}/sprites/blast_sprite.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite, 0.05)
        
        self.position_x: float
        self.position_y: float
        self.speed_x: float
        self.speed_y: float
        
        # Designamos um caminho (lane) aleatório ao blast
        self.lane = random.choice([
            game_constants.UP,
            game_constants.RIGHT,
            game_constants.DOWN,
            game_constants.LEFT,
        ])

        # Os que vêm de cima/baixo devem ser mais lentos, pois isso
        # compensa pela sua proximidade em relação ao player.
        angle_to_rotate_sprite: float = 0
        if self.lane == game_constants.UP:
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = 0
            self.speed_x = 0
            self.speed_y = speed / 1.75
            angle_to_rotate_sprite = 0

        elif self.lane == game_constants.RIGHT:
            self.position_x = game_constants.SCREEN_WIDTH
            self.position_y = game_constants.SCREEN_HEIGHT / 2
            self.speed_x = -speed
            self.speed_y = 0
            angle_to_rotate_sprite = 90

        elif self.lane == game_constants.DOWN:
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = game_constants.SCREEN_HEIGHT
            self.speed_x = 0
            self.speed_y = -1 * speed / 1.75
            angle_to_rotate_sprite = 0
        
        elif self.lane == game_constants.LEFT:
            self.position_x = 0
            self.position_y = game_constants.SCREEN_HEIGHT / 2
            self.speed_x = speed
            self.speed_y = 0
            angle_to_rotate_sprite = 90
                
        self.sprite = pygame.transform.rotate(self.sprite, angle_to_rotate_sprite)
        self.rect = self.sprite.get_rect(center=(self.position_x, self.position_y))
        
    def update(self):
        self.position_x += self.speed_x
        self.position_y += self.speed_y
        self.rect.center = ((self.position_x, self.position_y))

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
