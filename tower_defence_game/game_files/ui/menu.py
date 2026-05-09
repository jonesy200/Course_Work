import pygame

class Menu:
    def __init__(self, screen, buttons, width=180):
        self.screen = screen
        self.buttons = buttons
        self.open = False
        self.rect = pygame.Rect(
            screen.get_width() - width, 0, width, screen.get_height()
        )

    def toggle(self):
        self.open = not self.open

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.toggle()

    def draw(self):
        if not self.open:
            return None
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        for b in self.buttons:
            if b.draw(self.screen):
                return b
        return None