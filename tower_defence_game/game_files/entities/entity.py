import pygame

class Entity:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 1, 1)
        self.hitbox_colour = (255, 0, 0)

        self.image = None


    def check_collision(self, rect2):
        if self.rect.colliderect(rect2):
            print("detected collision")
            return True
        else:
            return False
