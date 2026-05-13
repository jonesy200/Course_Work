import pygame
from game_files.entities.units.friendly_units.friendly_unit import FriendlyUnit
from game_files.utils.settings import ANIMATION_FPS

class ChampionUnit(FriendlyUnit):
    def __init__(self, x, y, max_health=100, speed=2):
        super().__init__(x, y, max_health, speed)
        self.type = None

        self.state = "idle"
        self.frame_index = 0
        self.last_frame_time = 0

        self.animations = {
            "idle": [],
            "walk": [],
            "attack": [],
            "guard": [],
        }

        self.attack_damage = 25
        self.attack_range = 60
        self.attack_cooldown = 1000
        self.last_attack_time = 0

        self.projectiles = None

    def spawn(self, x, y):
        self.x = x
        self.y = y
        self.health = self.max_health
        self.set_state("idle")

    def despawn(self):
        self.health = 0

    def update(self):
        if not self.animations.get(self.state):
            return

        now = pygame.time.get_ticks()

        if self.state == "attack":
            frame_delay = 1000 // 5
        else:
            frame_delay = 1000 // ANIMATION_FPS

        if now - self.last_frame_time >= frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.state])
            self.last_frame_time = now

        if self.state == "attack" and self.frame_index == len(self.animations[self.state]) - 3 and self.type == 'archer':
            self.on_attack_finish()

        elif self.state == "attack" and self.frame_index == len(self.animations[self.state]) - 1:
            self.on_attack_finish()
            self.set_state("idle")

        '''if self.state == "attack" and self.frame_index == len(self.animations[self.state]) - 3 and self.type == "archer":
            self.on_attack_finish()
'''
    def move(self, dx, dy):
        super().move(dx, dy)
        if self.state not in ["attack"]:
            self.set_state("walk" if self.moving else "idle")

    def attack(self):
        pass

    def on_attack_finish(self):
        pass



