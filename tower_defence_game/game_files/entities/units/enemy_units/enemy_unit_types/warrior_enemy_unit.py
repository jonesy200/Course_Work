import pygame
from game_files.entities.units.enemy_units.enemy_unit import EnemyUnit
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import RED_UNITS_WARRIOR_DIR


class EnemyUnitWarrior(EnemyUnit):
    def __init__(self, x, y, max_health=100, speed=2):
        super().__init__(x, y, max_health, speed)

        self.path = RED_UNITS_WARRIOR_DIR
        self.sprite = Spritesheet("Warrior_Idle.png", path=self.path)
        self.walk_sprite = Spritesheet("Warrior_Run.png", path=self.path)
        self.attack1_sprite = Spritesheet("Warrior_Attack1.png", path=self.path)
        self.attack2_sprite = Spritesheet("Warrior_Attack2.png", path=self.path)
        self.guard_sprite = Spritesheet("Warrior_Guard.png", path=self.path)
        self.animations["idle"] = self.sprite.get_frames_row(0, 192, 192, 8)
        self.animations["walk"] = self.walk_sprite.get_frames_row(0, 192, 192, 6)
        self.animations["guard"] = self.guard_sprite.get_frames_row(0, 192, 192, 6)
        self.animations["attack1"] = self.attack1_sprite.get_frames_row(0,192,192,4)
        self.animations["attack2"] = self.attack2_sprite.get_frames_row(0,192,192,4)

    def update(self):
        self.moving = False

        self.move(self.direction * self.speed, 0)
        self.set_state("walk" if self.moving else "idle")
        super().update()

