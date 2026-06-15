from pathlib import Path
import os

#DIRECTORIES
BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = os.path.join(BASE_DIR,"assets")

IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

UI_IMAGES_DIR = os.path.join(IMAGES_DIR, "ui")
LOGOS_DIR = os.path.join(UI_IMAGES_DIR, "logos")

#TEMP DOWNLOADED ASSETS FOLDER
DOWNLOADED_ASSETS_DIR = os.path.join(ASSETS_DIR, "downloaded_from_online")
TINY_SWORDS_DIR = os.path.join(DOWNLOADED_ASSETS_DIR, "Tiny Swords (Free Pack)")

#PARTICLES
PARTICLE_DIR = os.path.join(TINY_SWORDS_DIR, "Particle FX")

#UI ELEMENTS
UI_ELEMENTS_DIR = os.path.join(TINY_SWORDS_DIR, "UI Elements", "UI Elements")

BUTTONS_DIR = os.path.join(UI_ELEMENTS_DIR, "Buttons")
PAPERS_DIR = os.path.join(UI_ELEMENTS_DIR, "Papers")

#TERRAIN
TERRAIN_DIR = os.path.join(TINY_SWORDS_DIR, "Terrain")
TILESET_DIR = os.path.join(TERRAIN_DIR, "Tileset")

#BUILDINGS
BUILDINGS_DIR = os.path.join(TINY_SWORDS_DIR, "Buildings")
BLACK_BUILDINGS_DIR = os.path.join(BUILDINGS_DIR, "Black Buildings")

#UNITS
UNITS_DIR = os.path.join(TINY_SWORDS_DIR, "Units")

BLACK_UNITS_DIR = os.path.join(UNITS_DIR, "Black Units")
BLACK_UNITS_WARRIOR_DIR = os.path.join(BLACK_UNITS_DIR, "Warrior")
BLACK_UNITS_ARCHER_DIR = os.path.join(BLACK_UNITS_DIR, "Archer")
BLACK_UNITS_ARCHER_ARROW_DIR = os.path.join(BLACK_UNITS_ARCHER_DIR, "Arrow.png")

RED_UNITS_DIR = os.path.join(UNITS_DIR, "Red Units")
RED_UNITS_WARRIOR_DIR = os.path.join(RED_UNITS_DIR, "Warrior")

BLUE_UNITS_DIR = os.path.join(UNITS_DIR, "Blue Units")
BLUE_UNITS_WARRIOR_DIR = os.path.join(BLUE_UNITS_DIR, "Warrior")
BLUE_UNITS_ARCHER_DIR = os.path.join(BLUE_UNITS_DIR, "Archer")
BLUE_UNITS_ARCHER_ARROW_DIR = os.path.join(BLUE_UNITS_ARCHER_DIR, "Arrow.png")

#ANIMATIONS
ANIMATION_FPS = 10 #10fps / 100ms

#CONSTANTS
WIDTH = 1600
HEIGHT = 1000
FPS = 60

TILE_SIZE = 128
GRASS_GREEN = (40, 120, 60)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BASE_LAYER = 0
PLAYER_LAYER = 1
MENU_LAYER = 3

g = 9.8
PROJECTILE_VELOCITY = 8

#DEBUG
HITBOXES = True
MACHINEGUN = True