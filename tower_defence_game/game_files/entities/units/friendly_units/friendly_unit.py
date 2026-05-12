import pygame
from game_files.entities.units.unit import Unit

class FriendlyUnit(Unit):
    def __init__(self, x, y, max_health=100, speed=2):
        super().__init__(x, y, max_health, speed)