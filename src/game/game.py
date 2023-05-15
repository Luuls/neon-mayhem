import pygame

from utility.utils import get_assets_path
from game import game_constants
from entities.blast import Blast
from entities.shield import Shield
from entities.player import Player

class Game():
    

    def __init__(self):
    # Controle da tela do jogo
        self.states = {
            'MENU': self.render_menu,
            'LEVEL': self.render_level,
            'GAMEOVER': 2
        }

        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        pygame.display.set_caption('Neon Mayhem')
        
        # Pega o path dos assets
        assets_path = get_assets_path(__file__)

        # Inicia o timer do blast
        self.blast_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.blast_timer, 750)

        # Inicia a lista do do blast
        self.blast_list = []

        # Inicializa as imagens do menu e do level
        menu_load = pygame.image.load(f'{assets_path}/backgrounds/menu_background.jpg').convert()
        self.menu_surface = pygame.transform.scale(
            menu_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        level_load = pygame.image.load(f'{assets_path}/backgrounds/level_background.jpg').convert()
        self.level_surface = pygame.transform.scale(
            level_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Inicializa o texto do menu
        self.title = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.title_surface = self.title.render(
            'NEON MAYHEM', True, '#01bfff'
        )
        self.title_rect = self.title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 50)
        )

        self.subtitle = self.title
        self.subtitle_surface = self.subtitle.render(
            'Press ENTER to play', True, '#01bfff'
        )
        self.subtitle_rect = self.subtitle_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 150)
        )

        self.copyright = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 17)
        self.copyright_surface = self.copyright.render(
            '2023 Nemesis Game Co. Published by M. R. Zatelli. All rights reserved.', True, 'White'
        )
        self.copyright_rect = self.copyright_surface.get_rect(
            bottomleft=(20, 702)
        )

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)
        pygame.mixer.music.play()

        self.current_state = 'MENU'
        self.render_state_screen = self.states[self.current_state]

        # cria as entidades do jogo
        self.player = Player()
        
    def screen_management(self) -> None:
        self.render_state_screen()
    
    def render_menu(self):
        self.screen.blit(self.menu_surface, (0, 0))

        self.screen.blit(self.title_surface, self.title_rect)
        self.screen.blit(self.subtitle_surface, self.subtitle_rect)
        self.screen.blit(self.copyright_surface, self.copyright_rect)

        pygame.display.flip()

    def render_level(self):
        self.screen.blit(self.level_surface, (0, 0))
        
        self.player.shield.draw_at(self.screen)

        self.player.draw_at(self.screen)

        for projectile in self.blast_list:
            projectile.draw_at(self.screen)
            projectile.update_position()

    def spawn_blast(self):
        
        new_blast = Blast('Blue', 10)
        self.blast_list.append(new_blast)