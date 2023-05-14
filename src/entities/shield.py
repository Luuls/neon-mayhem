from pygame import Surface, draw, Rect
from game import game_constants
# game_constants.SCREEN_WIDTH = x
# game_constants.SCREEN_HEIGHT = y

class Shield:

    # adicionar o parâmetro lane depois, talvez
    def __init__(self):
        self.direction = "RIGHT"
        self.color = "Blue"
        self.width = 100
        self.height = 10
        self.position_x = 0
        self.position_y = 0
        self.change_direction(self.direction)

    def change_direction(self, new_direction: str):
        self.direction = new_direction
        if new_direction == "UP":
            self.width = 100
            self.height = 10
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = (game_constants.SCREEN_HEIGHT / 2) - 50

        elif new_direction == "DOWN":
            self.width = 100
            self.height = 10
            self.position_x = game_constants.SCREEN_WIDTH / 2
            self.position_y = (game_constants.SCREEN_HEIGHT / 2) + 50

        elif new_direction == "LEFT":
            self.width = 10
            self.height = 100
            self.position_x = (game_constants.SCREEN_WIDTH / 2) - 50
            self.position_y = game_constants.SCREEN_HEIGHT / 2

        elif new_direction == "RIGHT":
            self.width = 10
            self.height = 100
            self.position_x = (game_constants.SCREEN_WIDTH / 2) + 50
            self.position_y = game_constants.SCREEN_HEIGHT / 2

    def draw_at(self, screen: Surface):
        # Cria o retângulo
        rect = Rect(0, 0, self.width, self.height)

        # Centraliza o retângulo na posição desejada
        rect.center = (self.position_x, self.position_y)

        draw.rect(screen, self.color, rect)