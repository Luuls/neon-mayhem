from utility.utils import get_assets_path
from entities.shield import Shield
from game import game_constants
from pygame import draw, image, Surface, transform
from entities.blast import Blast

class Player:

    def __init__(self):
        self.shield = Shield()
        self.health = 20
        self.radius = 30
        self.border = 0
        self.color = 'green'
        self.position_x = game_constants.SCREEN_WIDTH / 2
        self.position_y = game_constants.SCREEN_HEIGHT / 2

        # Carrega a imagem do player
        assets_path = get_assets_path(__file__)
        self.sprite = image.load(f'{assets_path}/sprites/player_sprite.png').convert_alpha()
        self.sprite = transform.scale(self.sprite, (150, 150))

        self.rect = self.sprite.get_rect()
        self.rect.center = (self.position_x, self.position_y)
        
    
    # muito sujeito á mudanças, apenas uma ideia inicial
    def damage(self) -> None:
        self.health -= 1
        if self.health == 0:
            self.is_alive = False

    def draw_at(self, screen: Surface):
        # Cria o círculo
        screen.blit(self.sprite, self.rect)

