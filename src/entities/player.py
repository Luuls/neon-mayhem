from utility.utils import get_assets_path

from game import game_constants
from entities.shield import Shield

from pygame import image, Surface, transform

class Player:
    def __init__(self):

        self.alive = True
        self.shield = Shield()
        self.health = 3
        self.position_x = game_constants.SCREEN_WIDTH / 2
        self.position_y = game_constants.SCREEN_HEIGHT / 2

        # Carrega a imagem do player
        assets_path = get_assets_path(__file__)
        self.sprite = image.load(f'{assets_path}/sprites/player_sprite.png').convert_alpha()
        self.sprite = transform.scale_by(self.sprite, 2.5)

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.position_x, self.position_y)
        
    # Função para computar o dano ao player
    def damage(self) -> None:
        self.health -= 1
        if self.health == 0:
            self.is_alive = False

    def draw_at(self, screen: Surface):
        screen.blit(self.sprite, self.rect)

