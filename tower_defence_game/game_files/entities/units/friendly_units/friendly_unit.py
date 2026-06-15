import pygame
from game_files.entities.units.unit import Unit

class FriendlyUnit(Unit):
    def __init__(self, game, x, y, max_health=100, speed=2, groups=None):
        super().__init__(game, x, y, max_health, speed, groups=[game.friendly_units])