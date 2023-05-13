import pygame
import entities

# Função para gerenciar o que será exibido na tela no estado atual
def screen_management(g_current_state, g_states, g_screen, g_title_surf, g_subtitle_surf, g_title_rect, g_subtitle_rect):
    if g_current_state == g_states['MENU']:
        g_screen.fill('Purple')
        g_screen.blit(g_title_surf, g_title_rect)
        g_screen.blit(g_subtitle_surf, g_subtitle_rect)
    
    elif g_current_state == g_states['LEVEL']:
        pygame.mixer.music.stop()
        
        g_screen.fill((48, 25, 52))
        pygame.draw.circle(g_screen, 'Yellow', (400, 300), 40)

        projectile = entities.Blast('Red', 0)
        projectile.blast_position()
        projectile.draw_blast(g_screen)

    pygame.display.flip()
