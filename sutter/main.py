import pygame
import functions

screen, states, current_state, title_surface, subtitle_surface = functions.load_game()

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and current_state == states['MENU']:
            current_state = states['LEVEL']

# Função para gerenciar a exibição na tela
    functions.screen_management(current_state, states, screen, title_surface, subtitle_surface)
    
    clock.tick(FPS)
        