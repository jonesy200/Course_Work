import pygame
import random
import os
from game_files.entities.units.enemy_units.enemy_unit_types.warrior_enemy_unit import EnemyUnitWarrior
from game_files.entities.units.friendly_units.champion_units.archer_champion_unit import ArcherChampionUnit
from game_files.entities.units.friendly_units.champion_units.warrior_champion_unit import WarriorChampionUnit
from game_files.systems.collision_grid import CollisionGrid
from game_files.entities.buildings.building import Building
from game_files.entities.buildings.castle import Castle
from game_files.ui.button import Button
from game_files.ui.menu import Menu
from game_files.utils.settings import (
    LOGOS_DIR,
    TILESET_DIR,
    WIDTH,
    HEIGHT,
    FPS,
    GRASS_GREEN,
    TILE_SIZE,
    BUTTONS_DIR,
    BLUE_UNITS_ARCHER_ARROW_DIR,
    MACHINEGUN,
    BLACK_BUILDINGS_DIR,
    BUILDING_SCALE
)


class TowerDefenceGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.showing_grid = False

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower Defence Game")
        icon_path = os.path.join(LOGOS_DIR, "grey shield logo.webp")
        self.icon = pygame.image.load(icon_path)
        pygame.display.set_icon(self.icon)
        self.background = self.create_background()

        blue_square_button_small_reg_path = os.path.join(BUTTONS_DIR, "SmallBlueSquareButton_Regular.png")
        blue_square_button_small_pressed_path = os.path.join(BUTTONS_DIR, "SmallBlueSquareButton_Pressed.png")
        black_castle_path = os.path.join(BLACK_BUILDINGS_DIR, "Castle.png")

        self.blue_square_button_small_reg_img = pygame.image.load(blue_square_button_small_reg_path).convert_alpha()
        self.blue_square_button_small_pressed_img = pygame.image.load(blue_square_button_small_pressed_path).convert_alpha()

        self.warrior_champion_spawn_button = Button(500, 1415, 10, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)
        self.archer_champion_spawn_button = Button(500, 1415, 100, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)

        self.enemy_spawn_button = Button(500, 1500, 10, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)
        self.spawn_castle_button = Button(500, 1500, 100, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)

        self.visualise_grid_button = Button(500, 1415, 190, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)

        self.champion = None
        self.champion_spawned = False

        self.menu = Menu(self.screen, [self.enemy_spawn_button, self.warrior_champion_spawn_button, self.archer_champion_spawn_button, self.spawn_castle_button, self.visualise_grid_button])
        self.collision_grid = CollisionGrid(self, self.width, self.height, cell_size=64)

        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.buildings = pygame.sprite.LayeredUpdates()
        self.castles = pygame.sprite.LayeredUpdates()
        self.towers = pygame.sprite.LayeredUpdates()
        self.houses = pygame.sprite.LayeredUpdates()

        self.units = pygame.sprite.LayeredUpdates()
        self.friendly_units = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.champions = pygame.sprite.LayeredUpdates()

        self.projectiles = pygame.sprite.LayeredUpdates()

        self.blocks = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

    def create_background(self):#
        background = pygame.Surface((self.width, self.height))
        background.fill(GRASS_GREEN)

        try:
            tileset_path = os.path.join(TILESET_DIR, "Tilemap_color1.png")
            tileset = pygame.image.load(tileset_path).convert_alpha()

            grass_tile = tileset.subsurface((24, 24, TILE_SIZE, TILE_SIZE))

            for y in range(0, self.height, TILE_SIZE):
                for x in range(0, self.width, TILE_SIZE):
                    background.blit(grass_tile, (x, y))

        except pygame.error as error:
            print(f"Could not load the tileset: {error}")

        return background

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu.toggle()

    def spawn_enemy(self, x=0, y=300):
        EnemyUnitWarrior(
            game= self,
            x=x,
            y=y,
            speed=2
        )

    def despawn_champion(self):
        if self.champion is not None:
            self.champion.kill()
            self.champion = None

        self.champion_spawned = False

    def spawn_building(self, x, y, max_health=1000):
        Building(
            game= self,
            x=x,
            y=y,
            max_health=max_health,
            asset_path=None
        )

    def spawn_castle(self, x, y, max_health=1000):
        Castle(
            game=self,
            x=x,
            y=y,
            scale=BUILDING_SCALE,
            max_health=max_health
        )

    def draw_buildings(self):
        self.buildings.draw(self.screen)

    def visualise_grid(self):
        self.showing_grid = True

    def remove_grid(self):
        self.showing_grid = False

    def update(self):
        keys = pygame.key.get_pressed()
        if self.champion_spawned:

            self.champion.moving = False

            if keys[pygame.K_BACKSPACE]:
                self.champion.health=0

            dx = dy = 0
            if keys[pygame.K_d]:
                dx += self.champion.speed
            if keys[pygame.K_a]:
                dx -= self.champion.speed
            if keys[pygame.K_w]:
                dy -= self.champion.speed
            if keys[pygame.K_s]:
                dy += self.champion.speed
            self.champion.move(dx, dy)

            if keys[pygame.K_SPACE]:
                self.champion.attack()
            if keys[pygame.K_r] and self.champion.type == 'archer' and MACHINEGUN == True:
                self.champion.machine_gun()
            if keys[pygame.K_g]:
                self.spawn_enemy(random.randint(50,1550), random.randint(50,950))
            if not self.champion.moving and self.champion.state not in ["attack", "guard", "death"]:
                self.champion.set_state("idle")

            if self.champion.death_finished:
                self.champion = None
                self.champion_spawned = False

        for projectile in self.projectiles:
            hit_enemies = pygame.sprite.spritecollide(projectile, self.enemies, False)

            for enemy in hit_enemies:
                if not enemy.dead:
                    enemy.take_damage(projectile.damage)
                    projectile.kill()
                    print("arrow collision")

        self.all_sprites.update()

        for enemy in self.enemies:
            if enemy.rect.left >= self.width:
                enemy.kill()

        for enemy in self.enemies:
            if enemy.death_finished:
                enemy.kill()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        if self.showing_grid:
            self.collision_grid.visualize_grid()

        clicked = self.menu.draw()
        if clicked == self.enemy_spawn_button:
            self.spawn_enemy()

        elif clicked == self.spawn_castle_button:
            self.spawn_castle(WIDTH // 2 , 160)

        elif clicked == self.visualise_grid_button:
            self.showing_grid = not self.showing_grid
            if self.showing_grid:
                self.visualise_grid()
            if not self.showing_grid:
                self.remove_grid()

        elif clicked == self.warrior_champion_spawn_button:
            if not self.champion_spawned:
                self.champion = WarriorChampionUnit(game=self,x=0, y=300)
                self.champion_spawned = True
                self.champion.spawn(WIDTH // 2, HEIGHT // 2)
            else: self.despawn_champion()

        elif clicked == self.archer_champion_spawn_button:
            if not self.champion_spawned:
                self.champion = ArcherChampionUnit(game=self,x=0, y=300)
                self.champion_spawned = True
                self.champion.spawn(WIDTH // 2, HEIGHT // 2)
            else: self.despawn_champion()

        for sprite in self.all_sprites:
            sprite.draw(self.screen)

            if hasattr(sprite, "draw_health") and not sprite.dead:
                sprite.draw_health(self.screen)

        self.draw_buildings()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            if not self.menu.open:
                self.update()
                self.playing = True
            else:
                self.playing = False
            self.draw()
