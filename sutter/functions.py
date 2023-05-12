import pygame
import classes

def load_game():

    pygame.init()

    # Controle da tela do jogo
    g_states = {
        'MENU': 0,
        'LEVEL': 1
    }

    g_current_state = g_states['MENU']

# Inicializa o display
    g_screen = pygame.display.set_mode((800, 600))
    g_screen.fill('Purple')
    pygame.display.set_caption('Neon Mayhem')

# Inicializa o texto do menu
    g_title = pygame.font.Font(None, 40)
    g_subtitle = pygame.font.Font(None, 40)
    g_title_surface = g_title.render('NEON MAYHEM', True, 'Yellow')
    g_subtitle_surface  = g_subtitle.render('Press ENTER to play', True, 'Yellow')

    return g_screen, g_states, g_current_state, g_title_surface, g_subtitle_surface


def screen_management(g_current_state, g_states, g_screen, g_title_surface, g_subtitle_surface):
    if g_current_state == g_states['MENU']:
        g_screen.fill('Purple')
        g_screen.blit(g_title_surface, (275, 150))
        g_screen.blit(g_subtitle_surface, (275, 250))
    
    elif g_current_state == g_states['LEVEL']:
        g_screen.fill((48, 25, 52))
        pygame.draw.circle(g_screen, 'Yellow', (400, 300), 40)

        projectile = classes.Blast('Red', 0)
        projectile.blast_position()
        projectile.draw_blast(g_screen)

    pygame.display.flip()
