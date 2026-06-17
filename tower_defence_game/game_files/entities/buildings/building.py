import pygame
import os
from game_files.entities.entity import Entity
from game_files.utils.settings import BLACK_BUILDINGS_DIR, HITBOXES, RED

class Building(Entity):
    def __init__(self, game, x, y, scale,max_health, asset_path, groups=None):
        super().__init__(game, None, x, y, groups=game.buildings)

        if asset_path == None:
            print("Error code 10: No asset path specified.")

        self.max_health = max_health
        self.health = max_health
        self.destroyed = False
        self.scale = scale

        self.path = asset_path
        image = pygame.image.load(self.path).convert_alpha()
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale))).convert_alpha()

        self.state = {
            "normal": self.image,
            "destroyed": []
        }

        self.current_state = "normal"

        self.rect = image.get_rect(center=(self.x, self.y))
        self.rect = self.rect.scale_by(self.scale)

        self.game.collision_grid.add_building(self)

    def update(self):
        if self.health < 0:
            self.current_state = "destroyed"
        else:
            self.current_state = "normal"

    def kill(self):
        self.game.collision_grid.remove_building(self)
        super().kill()

    def draw(self,screen):
        if self.current_state in self.state:

            screen.blit(self.state[self.current_state], self.rect)
        else:
            print(f"Error code 9: State '{self.current_state}' not found in building states.")

        if HITBOXES:
            pygame.draw.rect(screen, RED, self.rect, 2)
