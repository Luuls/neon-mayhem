import pygame
from game.game import Game

def main():
    # Instancia classe que iniciará o jogo
    game = Game()

    # Inicia o clock e define a taxa de frames
    clock = pygame.time.Clock()
    FPS = 60

    while True:

        # Laço para controlar o input do usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):

                pygame.quit()
                exit()

            # Dispara a condição para iniciar o level
            if game.current_state == game.states['MENU']:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        game.current_state = game.states['LEVEL']
            
            if game.current_state == game.states['LEVEL']:
                if event.type == game.blast_timer:
                    game.spawn_blast()
        
        # Controle do que é exibido na tela no estado atual
        game.screen_management()
        
        clock.tick(FPS)
        
if __name__ == '__main__':
    main()