import pygame
import os
from game_files.entities.buildings.building import Building
from game_files.utils.settings import BLACK_BUILDINGS_DIR

class Castle(Building):
    def __init__(self, game, x, y, max_health):
        super().__init__(game, x, y, max_health, groups=game.castles)

