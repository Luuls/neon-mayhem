import pygame
from game.game import Game

def main():
    # Instancia classe que iniciará o jogo
    game = Game()

    # Inicia o clock e define a taxa de frames
    clock = pygame.time.Clock()
    FPS = 60

    game.fade_menu()

    while True:

        # Laço para controlar o input do usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

            if event.type == game.game_timer:
                game.render_screen()

            # Dispara a condição para iniciar o level
            if game.get_current_state() == 'MENU':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        game.fade_level()
                        pygame.mixer.music.load(f'{game.assets_path}/songs/level_track.mp3')
                        pygame.mixer.music.play(-1)
                        game.set_current_state('LEVEL')
            
            if game.get_current_state() == 'LEVEL':
                if game.player.health <= 0:
                     game.set_current_state('GAME OVER')
                     pygame.mixer.music.stop()
                     gam_over_effect = pygame.mixer.Sound(f'{game.assets_path}/effects/game-over.mp3')
                     pygame.mixer.Sound.play(gam_over_effect)
                     game.render_game_over()
    
                if event.type == game.blast_timer:
                    game.blast_base_speed += game.speed_increment
                    game.spawn_blast()
                    
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        game.player.shield.update_shield_lane('UP')
                        
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        game.player.shield.update_shield_lane('DOWN')
                        
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        game.player.shield.update_shield_lane('LEFT')
                        
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        game.player.shield.update_shield_lane('RIGHT')


        # Controle do que é exibido na tela no estado atual
        #game.render_screen()
        #clock.tick(FPS)
        
if __name__ == '__main__':
    main()