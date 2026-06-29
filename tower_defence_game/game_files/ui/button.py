import pygame
from game_files.utils.settings import HITBOXES, WHITE

class Button:
    def __init__(self, press_time, x, y, image, clicked_image, scale=1, text="no text"):
        width, height = image.get_width(), image.get_height()

        self.press_time = press_time

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))).convert_alpha()
        self.clicked_image = pygame.transform.scale(clicked_image, (int(clicked_image.get_width() * scale), int(clicked_image.get_height() * scale))).convert_alpha()

        self.image_rect = self.image.get_rect(topleft=(x, y))
        self.text = text
        self.font = pygame.font.SysFont("Helvetica", 12)
        self.color = WHITE

        mask = pygame.mask.from_surface(self.image)
        bound = mask.get_bounding_rects()
        self.rect = (bound[0].move(x, y))

        self.clicked = False
        self.click_time = 0

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.clicked and self.click_time is not None:
            if pygame.time.get_ticks() - self.click_time >= self.press_time:
                self.clicked = False
                self.click_time = None

        if self.rect.collidepoint(pos):
            if HITBOXES == True:
                pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.click_time = pygame.time.get_ticks()
                action = True

        current_image = self.clicked_image if self.clicked else self.image
        screen.blit(current_image, self.image_rect)
        screen.blit(self.font.render(self.text, False, WHITE), (self.rect.x, self.rect.centery))

        return action

