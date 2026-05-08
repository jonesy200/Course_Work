import pygame
from game_files.utils.settings import WIDTH, HEIGHT, FPS

class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.rect = pygame.Rect(x, y, width, height)
        self.colour = (180, 40, 40)

    def update(self):
        self.x += self.speed
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
