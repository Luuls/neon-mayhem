import pygame

from states.state import State
import states.menu_state as menu_state
import subjects.keyboard_subject as keyboard_subject

from utility.utils import get_assets_path

from constants import game_constants

from entities.blast import Blast

class Game():
    def __init__(self):
        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Determina o caminho dos assets
        self.assets_path = get_assets_path(__file__)

        # Personaliza a janela do jogo
        pygame.display.set_caption('Neon Mayhem')
        self.icon_load = pygame.image.load(f'{self.assets_path}/icon/icon.jpg').convert()
        pygame.display.set_icon(self.icon_load)

        # Determina a velocidade base do blast e o incremento dela
        self.blast_base_speed = 7
        self.speed_increment = 0.0236

        # Cria timer do game
        self.game_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.game_timer, 16)

        # Inicializa as imagens do menu, do level e do game over
        menu_load = pygame.image.load(f'{self.assets_path}/backgrounds/menu_background.jpg').convert()
        self.menu_surf = pygame.transform.scale(
            menu_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        level_load = pygame.image.load(f'{self.assets_path}/backgrounds/level_background.jpg').convert()
        self.level_surf = pygame.transform.scale(
            level_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        over_load = pygame.image.load(f'{self.assets_path}/backgrounds/over_background.jpg').convert()
        self.over_surf = pygame.transform.scale(
            over_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Inicializa o texto do menu
        self.title = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 70)
        self.title_surf = self.title.render(
            'NEON MAYHEM', True, '#01bfff'
        )
        self.title_rect = self.title_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 50)
        )

        self.subtitle = self.title
        self.subtitle_surf = self.subtitle.render(
            'Press ENTER to play', True, '#01bfff'
        )
        self.subtitle_rect = self.subtitle_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 150)
        )

        self.blink_flag = True
        self.subtitle_alpha = 255

        # Inicializa o texto da tela de game over
        self.game_over_title = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 70)
        self.game_over_title_surf = self.game_over_title.render(
            'GAME OVER', True, '#01bfff'
        )
        
        self.game_over_retry_surf = self.game_over_title.render(
            'PRESS ANY KEY TO CONTINUE', True, '#01bfff'
        )

        self.game_over_title_rect = self.game_over_title_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 - 20)
        )

        self.game_over_retry_rect = self.game_over_retry_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, game_constants.SCREEN_HEIGHT / 2 + 55)
        )

        self.copyright = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 17)
        self.copyright_surf = self.copyright.render(
            '2023 Nemesis Game Co. Published by M. R. Zatelli. All rights reserved.', True, 'White'
        )
        self.copyright_rect = self.copyright_surf.get_rect(
            bottomleft=(20, 702)
        )

        # Inicializa o texto do número de vidas
        self.lives_text = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 25)
    
        # Inicializa a fonte da animação no começo do jogo
        self.intro_credits = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 70)
        self.intro_credits_2 = pygame.font.Font(f'{self.assets_path}/fonts/game_font.ttf', 70)

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{self.assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)

        # não registra nenhum evento na fila de eventos
        pygame.event.set_blocked(None)
        # Inicializa os efeitos sonoros
        self.shield_impact = pygame.mixer.Sound(f'{self.assets_path}/effects/shield_impact.wav')
        self.shield_impact.set_volume(0.10)
        self.damage_sound = pygame.mixer.Sound(f'{self.assets_path}/effects/damage.wav')
        self.press_sound = pygame.mixer.Sound(f'{self.assets_path}/effects/press.wav')

        self.keyboard_listener = keyboard_subject.KeyBoardSubject()

        self.current_state: State = menu_state.MenuState(self)
        self.current_state.entering()

        # Cria a superfície para fazer os fade-ins e outs
        self.fade = pygame.Surface((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.fade.fill((0, 0, 0))

    def run(self):
        # Inicia o clock e define a taxa de frames
        clock = pygame.time.Clock()

        while True:
            self.keyboard_listener.handle_events()
            self.update(self.keyboard_listener.keys_pressed)
            self.render()
            clock.tick(game_constants.FPS)
        
    def get_current_state(self) -> State:
        return self.current_state

    def set_state(self, new_state: State) -> None:
        self.current_state.exiting()
        self.current_state = new_state
        self.current_state.entering()
        
    def update(self, keys_pressed: list[int]):
        self.current_state.update(keys_pressed)
    
    def render(self) -> None:
        self.current_state.render()
        pygame.display.flip()
