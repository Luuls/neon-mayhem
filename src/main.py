import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True
    dt = 0
    pass

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("purple")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()

if __name__ == '__main__':
    main()