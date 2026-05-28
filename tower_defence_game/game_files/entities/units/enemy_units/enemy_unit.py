import pygame
from game_files.entities.units.unit import Unit
from game_files.systems.spritesheet import Spritesheet

class EnemyUnit(Unit):
    def __init__(self,game, x, y, max_health=100, speed=2):
        super().__init__(game, x, y, max_health, speed, groups=[game.enemies])