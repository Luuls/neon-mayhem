import pygame
# Classe para iniciar o jogo
class Game():

    def __init__(self):

        pygame.init()

        # Controle da tela do jogo
        self.states = {
        'MENU': 0,
        'LEVEL': 1
        }

        self.current_state = self.states['MENU']

        # Inicializa o display
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill('Purple')
        pygame.display.set_caption('Neon Mayhem')

        # Inicializa o texto do menu
        self.title = pygame.font.Font(None, 40)
        self.title_surf = self.title.render('NEON MAYHEM', True, 'Yellow')
        self.title_rect = self.title_surf.get_rect(center=(400, 50))

        self.subtitle = pygame.font.Font(None, 40)
        self.subtitle_surf  = self.subtitle.render('Press ENTER to play', True, 'Yellow')
        self.subtitle_rect = self.subtitle_surf.get_rect(center=(400, 90))

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load('../assets/menu_track.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
