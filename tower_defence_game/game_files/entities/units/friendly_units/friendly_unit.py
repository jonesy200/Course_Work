import pygame
from game_files.entities.units.unit import Unit

class FriendlyUnit(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)