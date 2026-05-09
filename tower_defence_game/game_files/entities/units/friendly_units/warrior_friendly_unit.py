import pygame
from game_files.entities.units.friendly_units.friendly_unit import FriendlyUnit

class PlayerWarriorUnit(FriendlyUnit):
    def __init__(self, x, y):
        super().__init__(x, y)


