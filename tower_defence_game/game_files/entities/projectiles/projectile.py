import pygame
from game_files.utils.settings import g, PROJECTILE_VELOCITY

class Projectile:
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing

        self.vel = PROJECTILE_VELOCITY

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.radius)

