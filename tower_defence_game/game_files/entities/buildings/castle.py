import pygame
import os
from game_files.entities.buildings.building import Building
from game_files.utils.settings import BLACK_BUILDINGS_DIR

class Castle(Building):
    def __init__(self, game, x, y, max_health, asset_path=os.path.join(BLACK_BUILDINGS_DIR, "Castle.png")):
        super().__init__(game, x, y, max_health, asset_path, groups=game.castles)

        self.path = BLACK_BUILDINGS_DIR, "Castle.png"