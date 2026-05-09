import pygame
from game_files.utils.settings import BLACK_UNITS_WARRIOR_DIR

pygame.init()
sheet = pygame.image.load(BLACK_UNITS_WARRIOR_DIR / "Warrior_Idle.png")
print(sheet.get_size())
pygame.quit()