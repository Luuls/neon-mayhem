from pygame import Surface, draw, Rect, image, transform
from game import game_constants
from utility.utils import get_assets_path
# game_constants.SCREEN_WIDTH = x
# game_constants.SCREEN_HEIGHT = y

class Shield():

    # adicionar o parâmetro lane depois, talvez
    def __init__(self):
         
        assets_path = get_assets_path(__file__)
        self.sprite = image.load(f'{assets_path}/sprites/shield_sprite.png').convert_alpha()

    
    def update_shield_lane(self, lane):

        self.lane = lane

        if self.lane == 'RIGHT':
            self.shield_sprite = transform.rotozoom(self.sprite, 0 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 + 120, game_constants.SCREEN_HEIGHT / 2)


        if self.lane == 'LEFT':
            self.shield_sprite = transform.rotozoom(self.sprite, 0 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 - 120, game_constants.SCREEN_HEIGHT / 2)

        if self.lane == 'UP':
            self.shield_sprite = transform.rotozoom(self.sprite, 90 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 - 120)

        if self.lane == 'DOWN':
            self.shield_sprite = transform.rotozoom(self.sprite, 90 , 0.06)
            self.shield_rect = self.shield_sprite.get_rect()
            self.shield_rect.center = (game_constants.SCREEN_WIDTH / 2 + 10, game_constants.SCREEN_HEIGHT / 2 + 120)