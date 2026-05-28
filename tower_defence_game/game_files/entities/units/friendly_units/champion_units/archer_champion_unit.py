import pygame
from game_files.entities.units.friendly_units.champion_units.champion_unit import ChampionUnit
from game_files.entities.projectiles.projectile import Projectile
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import BLACK_UNITS_ARCHER_DIR, BLACK_UNITS_ARCHER_ARROW_DIR, MACHINEGUN

class ArcherChampionUnit(ChampionUnit):
    def __init__(self,game, x, y):
        super().__init__(game, x, y, max_health=80, speed=3)
        self.type = "archer"
        self.arrow_img = pygame.image.load(BLACK_UNITS_ARCHER_ARROW_DIR).convert_alpha()

        self.path = BLACK_UNITS_ARCHER_DIR
        self.sprite = Spritesheet("Archer_Idle.png", path=self.path)
        self.walk_sprite = Spritesheet("Archer_Run.png", path=self.path)
        self.attack_sprite = Spritesheet("Archer_Shoot.png", path=self.path)

        self.animations["idle"] = self.sprite.get_frames_row(0, 192, 192, 6)
        self.animations["walk"] = self.walk_sprite.get_frames_row(0, 192, 192, 4)
        self.animations["attack"] = self.attack_sprite.get_frames_row(0, 192, 192, 8)


    def on_attack_finish(self):
        if self.arrow_img is None:
            print("missing arrow image")
            return

        print("arrow fired")

        if self.direction == 1:
            spawn_x = self.rect.right
        else:
            spawn_x = self.rect.left

        spawn_y = self.rect.centery

        self.spawn_projectile(self.arrow_img, spawn_x, spawn_y)


    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time >= self.attack_cooldown:
            self.last_attack_time = now
            self.set_state("attack")

    def machine_gun(self):
        if self.direction == 1:
            spawn_x = self.rect.right
        else: spawn_x = self.rect.left

        spawn_y = self.rect.centery
        self.spawn_projectile(self.arrow_img, spawn_x, spawn_y)

    def spawn_projectile(self,arrow_img, x, y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        projectile = Projectile(
            self.game,
            x,
            y,
            target_x=mouse_x,
            target_y=mouse_y,
            image=arrow_img
        )
        return projectile