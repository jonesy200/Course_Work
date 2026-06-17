import math
import pygame

class CollisionGrid:
    def __init__(self, game, world_width, world_height, cell_size=64):
        self.game = game

        self.world_width = world_width
        self.world_height = world_height
        self.cell_size = cell_size

        self.grid_cols = math.ceil(world_width / cell_size)
        self.grid_rows = math.ceil(world_height / cell_size)

        self.grid_node_width = 64
        self.grid_node_height = 64

        self.grid = []
        for i in range(self.grid_rows):
            row = []
            for j in range(self.grid_cols):
                row.append(0)

            self.grid.append(row)

        for row in self.grid:
            print(*row, sep="\t")

        self.squares = pygame.sprite.LayeredUpdates()

    def create_square(self, x, y, color):
        Square(self.game, self, x, y, color,groups=self.squares)

    def visualize_grid(self):
        y = 0
        for row in self.grid:
            x = 0
            for item in row:
                if item == 0:
                    self.create_square(x, y, (255, 255, 255))
                else:
                    self.create_square(x, y, (0, 0, 0))

                x += self.grid_node_width
            y += self.grid_node_height

    def remove_grid(self):
        for square in self.squares:
            square.kill()

class Square:
    def __init__(self, game, collision_grid, x, y, color, groups=None):
        self.x = x
        self.y = y
        self.color = color
        self.game = game
        self.collision_grid = collision_grid

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, [self.x, self.y, self.collision_grid.grid_node_width, self.collision_grid.grid_node_height])