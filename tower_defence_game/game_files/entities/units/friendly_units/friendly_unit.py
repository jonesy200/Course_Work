import pygame
from game_files.entities.units.unit import Unit

class FriendlyUnit(Unit):
    def __init__(self, game, x, y, max_health=100, speed=2, groups=None):
        if groups is None:
            groups = []

        super().__init__(game, x, y, max_health, speed, groups)