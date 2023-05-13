import pygame
import entities
from game_classes import Game

# Função para gerenciar o que será exibido na tela no estado atual
def screen_management(game: Game) -> None:
    if game.current_state == game.states['MENU']:
        game.screen.fill('Purple')
        game.screen.blit(game.title_surf, game.title_rect)
        game.screen.blit(game.subtitle_surf, game.subtitle_rect)
    
    elif game.current_state == game.states['LEVEL']:
        pygame.mixer.music.stop()
        
        game.screen.fill((48, 25, 52))
        pygame.draw.circle(game.screen, 'Yellow', (400, 300), 40)

        projectile = entities.Blast('Red', 0)
        projectile.blast_position()
        projectile.draw_blast(game.screen)

    pygame.display.flip()
