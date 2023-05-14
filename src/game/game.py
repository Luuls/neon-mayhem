import pygame

from game import game_constants
from entities.blast import Blast

class Game():
    # Controle da tela do jogo
    states = {
        'MENU': 0,
        'LEVEL': 1,
        'GAMEOVER': 3
    }

    def __init__(self):
        pygame.init()
        self.states

        self.current_state = self.states['MENU']

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        self.screen.fill('Purple')
        pygame.display.set_caption('Neon Mayhem')

        # Inicializa o texto do menu
        self.title = pygame.font.Font(None, 40)
        self.title_surface = self.title.render('NEON MAYHEM', True, 'Yellow')
        self.title_rect = self.title_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 50)
        )

        self.subtitle = pygame.font.Font(None, 40)
        self.subtitle_surface = self.subtitle.render(
            'Press ENTER to play', True, 'Yellow'
        )
        self.subtitle_rect = self.subtitle_surface.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 90)
        )

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load('../assets/menu_track.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
        
    def screen_management(self) -> None:
        if self.current_state == self.states['MENU']:
            self.screen.fill('Purple')
            self.screen.blit(self.title_surface, self.title_rect)
            self.screen.blit(self.subtitle_surface, self.subtitle_rect)
        
        elif self.current_state == self.states['LEVEL']:
            self.screen.fill((48, 25, 52))
            pygame.draw.circle(
                self.screen,
                'Yellow', 
                (game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_WIDTH / 2), 
                40
            )

            projectile = Blast('Red', 0)
            projectile.blast_position()
            projectile.draw_blast(self.screen)

        pygame.display.flip()
