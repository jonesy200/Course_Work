import pygame
from game_files.game import TowerDefenceGame

def main():
    pygame.init()
    game = TowerDefenceGame()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()