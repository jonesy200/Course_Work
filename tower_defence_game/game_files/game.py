import pygame
from game_files.entities.enemy import Enemy
from game_files.utils.button import Button
from game_files.utils.settings import (
    LOGOS_DIR,
    TILESET_DIR,
    WIDTH,
    HEIGHT,
    FPS,
    GRASS_GREEN,
    TILE_SIZE,
    BUTTONS_DIR
)

blue_square_button_small_reg_path = BUTTONS_DIR / "SmallBlueSquareButton_Regular.png"
blue_square_button_small_pressed_path = BUTTONS_DIR / "SmallBlueSquareButton_Pressed.png"

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

        self.background = self.create_backround()

        self.blue_square_button_small_reg_img = pygame.image.load(blue_square_button_small_reg_path).convert_alpha()
        self.blue_square_button_small_pressed_img = pygame.image.load(blue_square_button_small_pressed_path).convert_alpha()
        self.button1 = Button(500,20, 20, self.blue_square_button_small_reg_img, self.blue_square_button_small_pressed_img, 0.8)


        self.enemies = []


    def create_backround(self):#
        backround = pygame.Surface((self.width, self.height))
        backround.fill(GRASS_GREEN)

        try:
            tileset_path = TILESET_DIR / "Tilemap_color1.png"
            tileset = pygame.image.load(tileset_path).convert_alpha()

            grass_tile = tileset.subsurface((24, 24, TILE_SIZE, TILE_SIZE))

            for y in range(0, self.height, TILE_SIZE):
                for x in range(0, self.width, TILE_SIZE):
                    backround.blit(grass_tile, (x, y))

        except pygame.error as error:
            print(f"Could not load the tileset: {error}")

        return backround

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def spawn_enemy(self):
        enemy = Enemy(
            x=0,
            y=300,
            width=40,
            height=40,
            speed=2
        )
        self.enemies.append(enemy)

    def update(self):
        for enemy in self.enemies:
            enemy.update()

        self.enemies = [
            enemy for enemy in self.enemies
            if enemy.rect.left < self.width
        ]

    def draw(self):
        self.screen.blit(self.background, (0,0))

        if self.button1.draw(self.screen):
            self.spawn_enemy()
        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
