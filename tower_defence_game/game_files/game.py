import pygame
from game_files.entities.units.enemy_units.enemy_unit_types.warrior_enemy_unit import EnemyUnitWarrior
from game_files.entities.units.friendly_units.champion_units.archer_champion_unit import ArcherChampionUnit
from game_files.entities.units.friendly_units.champion_units.warrior_champion_unit import WarriorChampionUnit
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
    BLUE_UNITS_ARCHER_ARROW_DIR
)


class TowerDefenceGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.clock = pygame.time.Clock()
        self.running = True

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tower Defence Game")
        icon_path = LOGOS_DIR / "grey shield logo.webp"
        self.icon = pygame.image.load(icon_path)
        pygame.display.set_icon(self.icon)
        self.background = self.create_background()

        blue_square_button_small_reg_path = BUTTONS_DIR / "SmallBlueSquareButton_Regular.png"
        blue_square_button_small_pressed_path = BUTTONS_DIR / "SmallBlueSquareButton_Pressed.png"

        self.arrow_img = pygame.image.load(BLUE_UNITS_ARCHER_ARROW_DIR).convert_alpha()

        self.blue_square_button_small_reg_img = pygame.image.load(blue_square_button_small_reg_path).convert_alpha()
        self.blue_square_button_small_pressed_img = pygame.image.load(blue_square_button_small_pressed_path).convert_alpha()

        self.enemy_spawn_button = Button(500, 1500, 10, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)
        self.warrior_champion_spawn_button = Button(500, 1415, 10, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)
        self.archer_champion_spawn_button = Button(500, 1415, 80, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)

        self.enemies = []

        self.champion = None
        self.champion_spawned = False

        self.menu = Menu(self.screen, [self.enemy_spawn_button, self.warrior_champion_spawn_button, self.archer_champion_spawn_button])

        self.projectiles = []
        self.arrows = []

    def create_background(self):#
        background = pygame.Surface((self.width, self.height))
        background.fill(GRASS_GREEN)

        try:
            tileset_path = TILESET_DIR / "Tilemap_color1.png"
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

    def spawn_enemy(self):
        enemy = EnemyUnitWarrior(
            x=0,
            y=300,
            speed=2
        )
        self.enemies.append(enemy)

    def update(self):
        keys = pygame.key.get_pressed()
        if self.champion_spawned:
            colliders = []
            for e in self.enemies:
                colliders.append(e)

            self.champion.moving = False

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
            if not self.champion.moving and self.champion.state not in ["attack", "guard"]:
                self.champion.set_state("idle")
            self.champion.update()

            if self.enemies:
                for enemy in self.enemies:
                    if self.champion.check_collision(enemy.rect):
                        self.champion.hitbox_colour = (0, 255, 0)
                        print("unit collision")
                    else:
                        self.champion.hitbox_colour = (255, 0, 0)
                    for projectile in self.projectiles:
                        if projectile.check_collision(enemy.rect):
                            enemy.take_damage(projectile.damage)
                            projectile.alive = False
                            print("arrow collision")


        if self.champion_spawned:
            self.projectiles = [
                projectile for projectile in self.champion.projectiles
                if projectile.alive and not projectile.is_off_screen()
            ]

        self.enemies = [
            enemy for enemy in self.enemies
            if enemy.rect.left < self.width
        ]

        for enemy in self.enemies: enemy.update()
        for projectile in self.projectiles: projectile.update()

    def draw(self):
        self.screen.blit(self.background, (0,0))

        clicked = self.menu.draw()
        if clicked == self.enemy_spawn_button:
            self.spawn_enemy()
        elif clicked == self.warrior_champion_spawn_button:
            self.champion = WarriorChampionUnit(x=0, y=300)
            self.champion.projectiles = self.projectiles
            self.champion.arrow_img = self.arrow_img
            self.champion_spawned = not self.champion_spawned
            if self.champion_spawned:
                self.champion.spawn(WIDTH // 2, HEIGHT // 2)
            else:
                self.champion.despawn()

        elif clicked == self.archer_champion_spawn_button:
            self.champion = ArcherChampionUnit(x=0, y=300)
            self.champion.projectiles = self.projectiles
            self.champion.arrow_img = self.arrow_img
            self.champion_spawned = not self.champion_spawned
            if self.champion_spawned:
                self.champion.spawn(WIDTH // 2, HEIGHT // 2)
            else:
                self.champion.despawn()

        if self.champion_spawned:
            self.champion.draw(self.screen)

        for enemy in self.enemies: enemy.draw(self.screen)
        for projectile in self.projectiles: projectile.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            if not self.menu.open:
                self.update()
            self.draw()
