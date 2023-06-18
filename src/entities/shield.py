from __future__ import annotations

import pygame

from entities import player
from constants import shield_constants
from constants import game_constants

from utility.utils import get_assets_path

class Shield():
    def __init__(self, player_ref: player.Player):
        self.player = player_ref

        assets_path = get_assets_path(__file__)
        self.sprite = pygame.image.load(f'{assets_path}/sprites/shield_sprite.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite, 0.40)
        self.rect = self.sprite.get_rect()
        self.angle = 0
        
        # Escudo começa para cima
        self.move_shield(game_constants.UP)

    def move_shield(self, lane):
        # Rotaciona a sprite do escudo com a diferença de ângulo entre
        # a direção atual e a direção em que o escudo deve estar
        if lane == game_constants.UP:
            self.sprite = pygame.transform.rotate(self.sprite, 0 - self.angle)
            self.angle = 0

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x, 
                self.player.position_y - shield_constants.DISTANCE_FROM_PLAYER
            )

        elif lane == game_constants.RIGHT:
            self.sprite = pygame.transform.rotate(self.sprite, - 90 - self.angle)
            self.angle = -90

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x + shield_constants.DISTANCE_FROM_PLAYER, 
                self.player.position_y
            )
    
        elif lane == game_constants.LEFT:
            self.sprite = pygame.transform.rotate(self.sprite, 90 - self.angle)
            self.angle = 90

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x - shield_constants.DISTANCE_FROM_PLAYER, 
                self.player.position_y
            )

        elif lane == game_constants.DOWN:
            self.sprite = pygame.transform.rotate(self.sprite, 180 - self.angle)
            self.angle = 180

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x, 
                self.player.position_y + shield_constants.DISTANCE_FROM_PLAYER
            )

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
