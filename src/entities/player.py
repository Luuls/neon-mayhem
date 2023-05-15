from utility.utils import get_assets_path
from entities.shield import Shield
from game import game_constants
from pygame import draw, image, Surface
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
    
    # muito sujeito á mudanças, apenas uma ideia inicial
    def damage(self) -> None:
        self.health -= 1
        if self.health == 0:
    # alguma lógica pra dizer que morreu. Pode essa, por exemplo
            self.is_alive = False

    def draw_at(self, screen: Surface):
        # Carrega a imagem do player
        image_path = get_assets_path(__file__)  # image_path = get_assets_path(__file__) + '\\example_image.png'
        player_image = image.load(f'{image_path}/sprites/player_sprite.png')

        # Cria o círculo
        circulo = draw.circle(screen, self.color, (self.position_x, self.position_y), self.radius, self.border)

