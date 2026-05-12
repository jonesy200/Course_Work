import pygame
from game_files.entities.units.friendly_units.champion_units.champion_unit import ChampionUnit
from game_files.entities.projectiles.projectile import Projectile
from game_files.systems.spritesheet import Spritesheet
from game_files.utils.settings import BLACK_UNITS_ARCHER_DIR, BLACK_UNITS_ARCHER_ARROW_DIR

class ArcherChampionUnit(ChampionUnit):
    def __init__(self, x, y):
        super().__init__(x, y, max_health=80, speed=3)
        self.type = "archer"
        self.projectiles = None
        self.arrow_img = pygame.image.load(BLACK_UNITS_ARCHER_ARROW_DIR).convert_alpha()

        self.path = BLACK_UNITS_ARCHER_DIR
        self.sprite = Spritesheet("Archer_Idle.png", path=self.path)
        self.walk_sprite = Spritesheet("Archer_Run.png", path=self.path)
        self.attack_sprite = Spritesheet("Archer_Shoot.png", path=self.path)

        self.animations["idle"] = self.sprite.get_frames_row(0, 192, 192, 6)
        self.animations["walk"] = self.walk_sprite.get_frames_row(0, 192, 192, 4)
        self.animations["attack"] = self.attack_sprite.get_frames_row(0, 192, 192, 8)

    def on_attack_finish(self):
        if self.projectiles is None or self.arrow_img is None:
            return


        print("arrow fired")

        mouse_x, mouse_y = pygame.mouse.get_pos()

        spawn_x = self.rect.right if self.direction == 1 else self.rect.left
        spawn_y = self.rect.centery

        projectile = Projectile(
            spawn_x,
            spawn_y,
            target_x=mouse_x,
            target_y=mouse_y,
            image=self.arrow_img
        )
        self.projectiles.append(projectile)

    def attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_attack_time >= self.attack_cooldown:
            self.last_attack_time = now
            self.set_state("attack")