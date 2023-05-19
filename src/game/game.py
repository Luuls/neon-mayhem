import pygame

from utility.utils import get_assets_path
from game import game_constants
from entities.blast import Blast
from entities.shield import Shield
from entities.player import Player

class Game():
    

    def __init__(self):
        pygame.init()

        # Inicializa o display
        self.screen = pygame.display.set_mode(
            (game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT)
        )

        pygame.display.set_caption('Neon Mayhem')
        
        # Inicia o timer do blast
        self.blast_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.blast_timer, 470)

        assets_path = get_assets_path(__file__)
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

        self.intro_credits = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)
        self.intro_credits_2 = pygame.font.Font(f'{assets_path}/fonts/game_font.ttf', 70)

        # Inicializa trilha sonora do menu
        pygame.mixer.music.load(f'{assets_path}/songs/menu_track.mp3')
        pygame.mixer.music.set_volume(game_constants.MENU_VOLUME)
        pygame.mixer.music.play()

        # Controle da tela do jogo
        self.states = {
            'MENU': self.render_menu,
            'LEVEL': self.render_level
            # 'GAMEOVER': 2
        }

        self.current_state = 'MENU'
        self.render_state_screen = self.states[self.current_state]

        # cria as entidades do jogo e inicializa o escudo
        self.player = Player()
        self.player.shield.update_shield_lane('UP')

        # inicia a lista do do blast
        self.blast_list = []

        self.fade = pygame.Surface((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.fade.fill((0, 0, 0))


    def get_current_state(self) -> str:
        return self.current_state

    def set_current_state(self, new_state: str) -> None:
        self.current_state = new_state
        self.render_state_screen = self.states[self.current_state]
        
    def render_screen(self) -> None:
        self.render_state_screen()
        pygame.display.flip()
    
    def fade_menu(self):

        self.intro_credits_surf = self.intro_credits.render(
            'NEMESIS GAME COMPANY', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )

        for alpha in range(255, 0, -1):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        self.intro_credits_surf = self.intro_credits.render(
            'IN ASSOCIATION WITH', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 280)
        )

        for alpha in range(255, 0, -1):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        self.intro_credits_2_surf = self.intro_credits_2.render(
            'M. R. Zatelli and UFSC', True, 'Grey'
        )

        self.intro_credits_2_rect = self.intro_credits_2_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 390)
        )

        for alpha in range(255, 0, -1):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.intro_credits_2_surf, self.intro_credits_2_rect)
            self.screen.blit(self.fade, (0, 300))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.intro_credits_2_surf, self.intro_credits_2_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)

        self.intro_credits_surf = self.intro_credits.render(
            'PRESENT', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )

        for alpha in range(255, 0, -1):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(255, 0, -1):
            self.fade.set_alpha(alpha)
            self.render_menu()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
    
    def render_menu(self):
        self.screen.blit(self.menu_surface, (0, 0))

        self.screen.blit(self.title_surface, self.title_rect)
        self.screen.blit(self.subtitle_surface, self.subtitle_rect)
        self.screen.blit(self.copyright_surface, self.copyright_rect)

    def render_level(self):
        self.screen.blit(self.level_surface, (0, 0))
        
        self.screen.blit(self.player.shield.shield_sprite, self.player.shield.shield_rect)
        self.player.draw_at(self.screen)

        eliminated = []
                
        for i in range(len(self.blast_list)):
            self.blast_list[i].draw_at(self.screen)
            self.blast_list[i].update_position()

            if self.blast_list[i].blast_rect.colliderect(self.player.rect):
                print('Você foi atingido!')
                eliminated.append(self.blast_list[i])
                    
            elif self.blast_list[i].blast_rect.colliderect(self.player.shield.shield_rect):
                eliminated.append(self.blast_list[i])

        self.blast_list = [x for x in self.blast_list if x not in eliminated]

    def spawn_blast(self):
        
        new_blast = Blast('Blue', 10)
        self.blast_list.append(new_blast)