from utility.utils import get_assets_path
import sys

from constants import game_constants
from entities.shield import Shield

import pygame

class Player:
    def __init__(self):
        self.alive = True
        self.health = 3
        self.position_x = game_constants.SCREEN_WIDTH / 2
        self.position_y = game_constants.SCREEN_HEIGHT / 2
        self.shield = Shield(self)

        # Carrega a imagem do player
        assets_path = get_assets_path(__file__)
        self.sprite = pygame.image.load(f'{assets_path}/sprites/player_sprite.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite, 2.5)

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.position_x, self.position_y)

    def update(self, keys_pressed: list[int]):
        print(keys_pressed)
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key in [pygame.K_UP, pygame.K_w]:
                self.shield.move_shield('UP')
                
            elif key in [pygame.K_DOWN, pygame.K_s]:
                self.shield.move_shield('DOWN')
                
            elif key in [pygame.K_LEFT, pygame.K_a]:
                self.shield.move_shield('LEFT')
                
            elif key in [pygame.K_RIGHT, pygame.K_d]:
                self.shield.move_shield('RIGHT')
        
    def damage(self) -> None:
        self.health -= 1
        if self.health == 0:
            self.is_alive = False

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
