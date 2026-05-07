import pygame

class TowerDefenceGame:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tower Defence Game")

        programIcon = pygame.image.load('grey shield logo.webp')
        pygame.display.set_icon(programIcon)

        #clock = pygame.time.Clock()

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        screen.blit(background, (0, 0))
        pygame.display.flip()

        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            screen.blit(background, (0, 0))
            pygame.display.flip()

