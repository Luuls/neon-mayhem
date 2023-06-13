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
        assets_path = get_assets_path(__file__)

        # Personaliza a janela do jogo
        pygame.display.set_caption('Neon Mayhem')
        self.icon_load = pygame.image.load(f'{assets_path}/icon/icon.jpg').convert()
        pygame.display.set_icon(self.icon_load)

        # Cria timer do game
        self.game_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.game_timer, 16)

        # Inicializa as imagens do menu, do level e do game over
        menu_load = pygame.image.load(f'{assets_path}/backgrounds/menu_background.jpg').convert()
        self.menu_surface = pygame.transform.scale(
            menu_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )
        
        level_load = pygame.image.load(f'{assets_path}/backgrounds/level_background.jpg').convert()
        self.level_surface = pygame.transform.scale(
            level_load, (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        # Inicializa o texto do menu
        self.blink_flag = True
        self.subtitle_alpha = 255

        # Inicializa o texto do número de vidas
        self.lives_text = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 25)
    
        # Inicializa a fonte da animação no começo do jogo
        self.intro_credits = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.intro_credits_2 = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)

        # não registra nenhum evento na fila de eventos
        pygame.event.set_blocked(None)
        
        self.keyboard_listener = keyboard_subject.KeyBoardSubject()

        self.current_state: State = menu_state.MenuState(self)
        self.current_state.entering()

        # Cria a superfície para fazer os fade-ins e outs
        self.fade = pygame.Surface((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.fade.fill((0, 0, 0))

    def run(self):
        # Inicia o clock
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
