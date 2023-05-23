from __future__ import annotations

import pygame

from entities import player
from constants import shield_constants
# from game import game_constants
from utility.utils import get_assets_path

class Shield():
    def __init__(self, player_ref: player.Player):
        self.player = player_ref

        assets_path = get_assets_path(__file__)
        self.sprite = pygame.image.load(f'{assets_path}/sprites/shield_sprite.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite, (0.07, 0.1))
        self.sprite = pygame.transform.rotate(self.sprite, 90)

        self.rect = self.sprite.get_rect()
        self.angle = 0
        self.move_shield('UP')

    def move_shield(self, lane):
        if lane == 'RIGHT':
            self.sprite = pygame.transform.rotate(self.sprite, - 90 - self.angle)
            self.angle = -90

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x + shield_constants.DISTANCE_FROM_PLAYER, 
                self.player.position_y
            )

        elif lane == 'LEFT':
            self.sprite = pygame.transform.rotate(self.sprite, 90 - self.angle)
            self.angle = 90

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x - shield_constants.DISTANCE_FROM_PLAYER, 
                self.player.position_y
            )

        elif lane == 'UP':
            self.sprite = pygame.transform.rotate(self.sprite, 0 - self.angle)
            self.angle = 0

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x, 
                self.player.position_y - shield_constants.DISTANCE_FROM_PLAYER
            )

        elif lane == 'DOWN':
            self.sprite = pygame.transform.rotate(self.sprite, 180 - self.angle)
            self.angle = 180

            self.rect = self.sprite.get_rect()
            self.rect.center = (
                self.player.position_x, 
                self.player.position_y + shield_constants.DISTANCE_FROM_PLAYER
            )

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.sprite, self.rect)
