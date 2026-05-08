import pygame

class TowerDefenceGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.running = True

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower Defence Game")
        self.load_assets()

        try:
            self.icon = pygame.image.load('assets/images/ui/logos/grey shield logo.webp')
            pygame.display.set_icon(self.icon)
        except pygame.error as error:
            print(f"Could not load the icon: {error}")

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

    def load_assets(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
