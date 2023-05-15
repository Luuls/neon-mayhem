import pygame

from utility.utils import get_assets_path
from game import game_constants
from entities.blast import Blast
from entities.shield import Shield

class Game():
    
    # Controle da tela do jogo
    states = {
        'MENU': 0,
        'LEVEL': 1,
        'GAMEOVER': 3
    }

    def __init__(self):

        pygame.init()
        
        # Inicializa o escudo
        self.shield = Shield()

        # Determina o começo do jogo como sendo no menu
        self.current_state = self.states['MENU']

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        pygame.display.set_caption('Neon Mayhem')

        
        # Pega o path dos assets
        assets_path = get_assets_path(__file__)

        # Inicializa as imagens do menu e do level
        menu_load = pygame.image.load(f'{assets_path}/menu_background.jpg').convert()
        self.menu_surface = pygame.transform.scale(
            menu_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        level_load = pygame.image.load(f'{assets_path}/level_background.jpg').convert()
        self.level_surface = pygame.transform.scale(
            level_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Inicializa o texto do menu
        self.title = pygame.font.Font(f'{assets_path}/game_font.ttf', 70)
        self.title_surface = self.title.render(
            'NEON MAYHEM', True, '#01bfff'
        )
        self.title_rect = self.title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 50)
        )

        self.subtitle = pygame.font.Font(f'{assets_path}/game_font.ttf', 70)
        self.subtitle_surface = self.subtitle.render(
            'Press ENTER to play', True, '#01bfff'
        )
        self.subtitle_rect = self.subtitle_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 150)
        )

        self.copyright = pygame.font.Font(f'{assets_path}/game_font.ttf', 17)
        self.copyright_surface = self.copyright.render(
            '2023 Nemesis Game Co. Published by M. R. Zatelli. All rights reserved.', True, 'White'
        )
        self.copyright_rect = self.copyright_surface.get_rect(
            bottomleft=(20, 702)
        )

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)
        pygame.mixer.music.play()
        
    def screen_management(self) -> None:
        if self.current_state == self.states['MENU']:
            self.screen.blit(self.menu_surface, (0, 0))

            self.screen.blit(self.title_surface, self.title_rect)
            self.screen.blit(self.subtitle_surface, self.subtitle_rect)
            self.screen.blit(self.copyright_surface, self.copyright_rect)
        
        elif self.current_state == self.states['LEVEL']:
            
            self.screen.blit(self.level_surface, (0, 0))
            pygame.draw.circle(
                self.screen,
                'Yellow', 
                (game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2), 
                20
            )
            self.shield.draw_at(self.screen)

            projectile = Blast('Red', 0)
            projectile.draw_at(self.screen)

        pygame.display.flip()
