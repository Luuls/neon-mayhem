import pygame
import functions
import classes

game = classes.Game()

# Inicia o clock e define a taxa de frames
clock = pygame.time.Clock()
FPS = 60

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    # Dispara a condição para iniciar o level
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and game.current_state == game.states['MENU']:
            pygame.mixer.music.stop()
            game.current_state = game.states['LEVEL']

# Função para gerenciar a exibição na tela
    functions.screen_management(game.current_state, game.states, game.screen, game.title_surface, game.subtitle_surface)
    
    clock.tick(FPS)
        