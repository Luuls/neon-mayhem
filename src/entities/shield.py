from pygame import image, transform
from game import game_constants
from utility.utils import get_assets_path

class Shield():

    def __init__(self):
         
        assets_path = get_assets_path(__file__)
        self.sprite = image.load(f'{assets_path}/sprites/shield_sprite2.png').convert_alpha()
        self.sprite = transform.scale_by(self.sprite, 5.0)

    # Função para redesenhar o escudo conforme sua posição muda
    def update_shield_lane(self, lane):

        self.lane = lane

        if self.lane == 'RIGHT':
            self.shield_sprite = transform.rotozoom(self.sprite, 270 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 + 80, game_constants.SCREEN_HEIGHT / 2)


        if self.lane == 'LEFT':
            self.shield_sprite = transform.rotozoom(self.sprite, 90 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 - 80, game_constants.SCREEN_HEIGHT / 2)

        if self.lane == 'UP':
            self.shield_sprite = transform.rotozoom(self.sprite, 0 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 - 80)

        if self.lane == 'DOWN':
            self.shield_sprite = transform.rotozoom(self.sprite, 180 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 + 10, game_constants.SCREEN_HEIGHT / 2 + 80)
