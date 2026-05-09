import pygame
from game_files.entities.units.unit import Unit
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import BLACK_UNITS_WARRIOR_DIR


class WarriorChampionUnit(Unit):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.path = BLACK_UNITS_WARRIOR_DIR
        self.sprite = Spritesheet("Warrior_Idle.png", path=self.path)
        self.walk_sprite = Spritesheet("Warrior_Run.png", path=self.path)
        self.attack1_sprite = Spritesheet("Warrior_Attack1.png", path=self.path)
        self.attack2_sprite = Spritesheet("Warrior_Attack2.png", path=self.path)
        self.guard_sprite = Spritesheet("Warrior_Guard.png", path=self.path)
        self.animations["idle"] = self.sprite.get_frames_row(0, 192, 192, 8)
        self.animations["walk"] = self.walk_sprite.get_frames_row(0, 192, 192, 6)
        self.animations["guard"] = self.guard_sprite.get_frames_row(0, 192, 192, 6)
        self.animations["attack1"] = self.attack1_sprite.get_frames_row(0, 192, 192, 4)
        self.animations["attack2"] = self.attack2_sprite.get_frames_row(0, 192, 192, 4)

    def spawn(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 2
        self.set_state("idle")

    def despawn(self):
        self.health = 0

    def move_right(self):
        self.move(self.speed, 0)
        self.set_state("walk" if self.moving else "idle")

    def move_left(self):
        self.move(-self.speed, 0)
        self.set_state("walk" if self.moving else "idle")

    def move_up(self):
        self.move(0, -self.speed)
        self.set_state("walk" if self.moving else "idle")

    def move_down(self):
        self.move(0, self.speed)
        self.set_state("walk" if self.moving else "idle")

