from utility.utils import get_assets_path
import sys

from game import game_constants
from entities.shield import Shield

import pygame

class Player:
    def __init__(self):
        self.alive = True
        self.shield = Shield()
        self.health = 3
        self.position_x = game_constants.SCREEN_WIDTH / 2
        self.position_y = game_constants.SCREEN_HEIGHT / 2

        # Carrega a imagem do player
        assets_path = get_assets_path(__file__)
        self.sprite = pygame.image.load(f'{assets_path}/sprites/player_sprite.png').convert_alpha()
        self.sprite = pygame.transform.rotozoom(self.sprite, 0, 0.12)

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.position_x, self.position_y)

    def update(self, keys_pressed: list[int]):
        print(keys_pressed)
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_UP:
                self.shield.update_shield_lane('UP')
                
            elif key == pygame.K_DOWN:
                self.shield.update_shield_lane('DOWN')
                
            elif key == pygame.K_LEFT:
                self.shield.update_shield_lane('LEFT')
                
            elif key == pygame.K_RIGHT:
                self.shield.update_shield_lane('RIGHT')
        
    def damage(self) -> None:
        self.health -= 1
        if self.health == 0:
            self.is_alive = False

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
