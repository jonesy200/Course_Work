import pygame
import os
from game_files.entities.entity import Entity
from game_files.utils.settings import BLACK_BUILDINGS_DIR

class Building(Entity):
    def __init__(self, game, x, y, max_health, asset_path, groups=None):
        super().__init__(game, None, x, y, groups=game.buildings)

        if asset_path == None:
            print("Error code 10: No asset path specified.")

        self.max_health = max_health
        self.health = max_health
        self.destroyed = False

        self.path = asset_path
        self.image = pygame.image.load(self.path).convert_alpha()
        self.state = {
            "normal": self.image,
            "destroyed": []
        }

        self.current_state = "normal"

        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def update(self):
        if self.health < 0:
            self.current_state = "destroyed"
        else:
            self.current_state = "normal"

    def draw(self,screen):
        if self.current_state in self.state:
            screen.blit(self.state[self.current_state], self.rect)
        else:
            print(f"Error code 9: State '{self.current_state}' not found in building states.")

