import pygame
from game_files.entities.units.friendly_units.champion_units.champion_unit import ChampionUnit
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import BLACK_UNITS_WARRIOR_DIR

class WarriorChampionUnit(ChampionUnit):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.type = "warrior"

        self.path = BLACK_UNITS_WARRIOR_DIR
        self.sprite = Spritesheet("Warrior_Idle.png", path=self.path)
        self.walk_sprite = Spritesheet("Warrior_Run.png", path=self.path)
        self.attack_sprite = Spritesheet("Warrior_Attack1.png", path=self.path)
        self.guard_sprite = Spritesheet("Warrior_Guard.png", path=self.path)

        self.animations["idle"] = self.sprite.get_frames_row(0, 192, 192, 8)
        self.animations["walk"] = self.walk_sprite.get_frames_row(0, 192, 192, 6)
        self.animations["attack"] = self.attack_sprite.get_frames_row(0, 192, 192, 4)
        self.animations["guard"] = self.guard_sprite.get_frames_row(0, 192, 192, 6)

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time >= self.attack_cooldown:
            self.last_attack_time = now
            self.set_state("attack")


