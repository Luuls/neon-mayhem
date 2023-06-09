import pygame

from utility.utils import get_assets_path
from game import game_constants
from entities.blast import Blast
from entities.player import Player

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
        
        # Cria o player e inicializa o escudo
        self.player = Player()
        self.player.shield.update_shield_lane('UP')

        # Determina a velocidade base do blast e o incremento dela
        self.blast_base_speed = 7
        self.speed_increment = 0.0236

        # Cria o timer do blast
        self.blast_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.blast_timer, 470)

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
        pygame.mixer.music.play()

        # Inicializa os efeitos sonoros
        self.shield_impact = pygame.mixer.Sound(f'{self.assets_path}/effects/shield_impact.wav')
        self.shield_impact.set_volume(0.10)
        self.damage_sound = pygame.mixer.Sound(f'{self.assets_path}/effects/damage.wav')
        self.press_sound = pygame.mixer.Sound(f'{self.assets_path}/effects/press.wav')

        # Controle da tela do jogo
        self.states = {
            'MENU': self.render_menu,
            'LEVEL': self.render_level,
            'GAME OVER': self.render_game_over,
        }

        self.current_state = 'MENU'
        self.render_state_screen = self.states[self.current_state]

        # Inicia a lista do do blast
        self.blast_list = []

        # Cria a superfície para fazer os fade-ins e outs
        self.fade = pygame.Surface((game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT))
        self.fade.fill((0, 0, 0))

    
    # Funções para obter o estado atual/mudar o estado atual
    def get_current_state(self) -> str:
        return self.current_state

    def set_current_state(self, new_state: str) -> None:
        self.current_state = new_state
        self.render_state_screen = self.states[self.current_state]

    # Função para renderizar a tela do estado
    def render_screen(self) -> None:
        self.render_state_screen()
        pygame.display.flip()
    
    # Animação do começo do jogo
    def fade_menu(self):

        self.intro_credits_surf = self.intro_credits.render(
            'NEMESIS GAME COMPANY', True, 'Grey'
        )

        self.intro_credits_rect = self.intro_credits_surf.get_rect(
            center=(game_constants.SCREEN_WIDTH / 2, 360)
        )

        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return
            
            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return
            
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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return
            
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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.intro_credits_2_surf, self.intro_credits_2_rect)
            self.screen.blit(self.fade, (0, 300))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

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
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(0, 255):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

            self.fade.set_alpha(alpha)
            self.screen.blit(self.intro_credits_surf, self.intro_credits_rect)
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
        
        for alpha in range(255, 0, -1):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.press_sound)
                    return

            self.fade.set_alpha(alpha)
            self.render_menu()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(18)
    
    def blink_text(self):
        
        if self.blink_flag == True:
            self.subtitle_surf.set_alpha(self.subtitle_alpha)
            self.subtitle_alpha -= 3

            if self.subtitle_alpha <= 0:
                self.blink_flag = False
        
        if self.blink_flag == False:
            self.subtitle_surf.set_alpha(self.subtitle_alpha)
            self.subtitle_alpha += 3

            if self.subtitle_alpha >= 255:
                self.blink_flag = True
    

    def render_menu(self):
        self.screen.blit(self.menu_surf, (0, 0))

        self.screen.blit(self.title_surf, self.title_rect)
        self.screen.blit(self.subtitle_surf, self.subtitle_rect)
        self.blink_text()
        self.screen.blit(self.copyright_surf, self.copyright_rect)

    def render_level(self):
        self.screen.blit(self.level_surf, (0, 0))
        
        self.screen.blit(self.player.shield.shield_sprite, self.player.shield.shield_rect)
        self.player.draw_at(self.screen)

        self.lives_text_surf = self.lives_text.render(
            f'Lives: {self.player.health}', True, 'White'
        )
        self.lives_text_rect = self.lives_text_surf.get_rect(
            bottomleft=(40, 702)
        )


        self.screen.blit(self.lives_text_surf, self.lives_text_rect)        

        eliminated = []
                
        # Determinação de colisão do blast e atualização da posição
        for i in range(len(self.blast_list)):
            self.blast_list[i].draw_at(self.screen)
            self.blast_list[i].update_position()

            if self.blast_list[i].blast_rect.colliderect(self.player.rect):
                if self.player.health >= 2:
                    pygame.mixer.Sound.play(self.damage_sound)
                self.player.damage()
                eliminated.append(self.blast_list[i])
                    
            elif self.blast_list[i].blast_rect.colliderect(self.player.shield.shield_rect):
                pygame.mixer.Sound.play(self.shield_impact)
                eliminated.append(self.blast_list[i])

        # Eliminamos os que colidiram
        self.blast_list = [x for x in self.blast_list if x not in eliminated]

    def render_game_over(self):

        if self.player.health <= 0:
            self.player.health = 3
        
        if len(self.blast_list) != 0:
            self.blast_list.clear()

        self.screen.blit(self.over_surf, (0, 0))
        self.screen.blit(self.game_over_title_surf, self.game_over_title_rect)
        self.screen.blit(self.game_over_retry_surf, self.game_over_retry_rect)

    def fade_game_over(self):

        for alpha in range(0, 255):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.render_game_over()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2)

        for alpha in range(255, 0, -1):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.render_menu()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2)

    # Transição entre o menu e o level
    def fade_level(self):

        for alpha in range(0, 255):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.render_menu()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2)

        for alpha in range(255, 0, -1):
            pygame.event.get()
            self.fade.set_alpha(alpha)
            self.render_level()
            self.screen.blit(self.fade, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2)

    # Função que cuida da geração de blasts
    def spawn_blast(self):
        new_blast = Blast('Blue', self.blast_base_speed)
        self.blast_list.append(new_blast)