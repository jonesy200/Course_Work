import pygame
from game_files.entities.units.unit import Unit
from game_files.systems.spritesheet import Spritesheet

class EnemyUnit(Unit):
    def __init__(self, x, y, max_health=100, speed=10):
        super().__init__(x, y, max_health, speed)