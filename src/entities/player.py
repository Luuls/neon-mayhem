from game.game import get_assets_path
from entities.shield import Shield
from game import game_constants
from pygame import draw, image, Surface

class Player:

    def __init__(self):
        self.shield = Shield()
        self.health = 20
        self.size = (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT, 50, 3)
        self.color = 'Purple'
        self.position_x = game_constants.SCREEN_WIDTH / 2
        self.position_y = game_constants.SCREEN_HEIGHT / 2

    def draw_at(self, screen: Surface):
        # Carrega a imagem do player
        player = image.load(f'{get_assets_path.assets_path}/player.png')
        # Cria o círculo
        circulo = draw.circle(50, 2)
        # Desenha o cìrculo
        draw.circle = (screen, circulo)