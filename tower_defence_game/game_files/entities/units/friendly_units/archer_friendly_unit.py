import pygame
from game_files.entities.units.enemy_units.enemy_unit import EnemyUnit
from game_files.entities.units.friendly_units.friendly_unit import FriendlyUnit
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import BLUE_UNITS_ARCHER_DIR

class FriendlyUnitArcher(FriendlyUnit):
    def __init__(self, x, y, max_health=60, speed=3):
        super().__init__(self, x, y, max_health, speed)

        self.path = BLUE_UNITS_ARCHER_DIR
        self.sprite = Spritesheet("Archer_Idle",path=self.path)
        self.walk_sprite = Spritesheet("Archer_Run",path=self.path)
        self.shoot_sprite = Spritesheet("Archer_Shoot",path=self.path)

