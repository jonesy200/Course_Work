import math
import pygame
from game_files.utils.settings import (
RED,
GREEN,
BLUE,
WHITE,
BLACK
)

class CollisionGrid:
    def __init__(self, game, world_width, world_height, cell_size=16):
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

    def visualize_grid(self):
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                color = WHITE if self.grid[row][col] == 0 else BLACK

                pygame.draw.rect(
                    self.game.screen,
                    color,
                    (
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1
                )

    def remove_grid(self):
        for square in self.squares:
            square.kill()
