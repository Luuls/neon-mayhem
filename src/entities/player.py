from utility.utils import get_assets_path
import sys

from constants import game_constants
from entities.shield import Shield

import pygame

class Player:
    def __init__(self):
        self.is_alive: bool = True
        self.health: int = 3
        
        self.position_x: float = game_constants.SCREEN_WIDTH / 2
        self.position_y: float = game_constants.SCREEN_HEIGHT / 2
        
        self.shield = Shield(self)
        
        self.score: int = 0
        self.score_multiplier: float  = 1

        # Carrega a imagem do player
        assets_path = get_assets_path(__file__)
        self.sprite = pygame.image.load(f'{assets_path}/sprites/player_sprite.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite, 2.5)

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.position_x, self.position_y)

    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key in [pygame.K_UP, pygame.K_w]:
                self.shield.move_shield(game_constants.UP)
                
            elif key in [pygame.K_RIGHT, pygame.K_d]:
                self.shield.move_shield(game_constants.RIGHT)
                
            elif key in [pygame.K_DOWN, pygame.K_s]:
                self.shield.move_shield(game_constants.DOWN)
                
            elif key in [pygame.K_LEFT, pygame.K_a]:
                self.shield.move_shield(game_constants.LEFT)
        
    # Função para computar o dano ao player
    def damage(self) -> None:
        if not self.is_alive:
            return 

        if self.health == 1:
            self.is_alive = False

        self.health -= 1
        self.score_multiplier = 1

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
