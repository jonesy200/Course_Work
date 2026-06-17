# Source - https://stackoverflow.com/a/64458774
# Posted by Cribber, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-17, License - CC BY-SA 4.0

import pygame
import random
running = True

gridDisplay = pygame.display.set_mode((200, 200))
pygame.display.get_surface().fill((200, 200, 200))  # background

rows = 12
cols = 16
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        i = i + 1
        row.append(random.randint(0,1))

    matrix.append(row)

for row in matrix:
    print(*row, sep="\t")

# we use the sizes to draw as well as to do our "steps" in the loops.
grid_node_width = 10
grid_node_height = 10

def createSquare(x, y, color):
    pygame.draw.rect(gridDisplay, color, [x, y, grid_node_width, grid_node_height ])



def visualizeGrid():
    y = 0  # we start at the top of the screen
    for row in matrix:
        x = 0 # for every row we start at the left of the screen again
        for item in row:
            if item == 0:
                createSquare(x, y, (255, 255, 255))
            else:
                createSquare(x, y, (0, 0, 0))

            x += grid_node_width # for ever item/number in that row we move one "step" to the right
        y += grid_node_height   # for every new row we move one "step" downwards
    pygame.display.update()


visualizeGrid()  # call the function
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
