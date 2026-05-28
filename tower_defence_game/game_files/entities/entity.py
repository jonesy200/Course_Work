import pygame
from game_files.utils.settings import RED

class Entity(pygame.sprite.Sprite):
    def __init__(self, game, screen, x, y, groups=None):
        if groups is None:
            groups = []

        super().__init__(game.all_sprites, *groups)

        self.game = game
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 1, 1)
        self.hitbox_colour = (255, 0, 0)

        self.image = pygame.Surface((192, 192))
        self.image.fill(RED)

    def update(self):
        pass

    def check_collision(self, rect2):
        if self.rect.colliderect(rect2):
            print("detected collision")
            return True
        else:
            return False
