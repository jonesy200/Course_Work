import pygame

import path
import sys

directory = path.path(__file__).abspath()
sys.path.append(directory.parent.parent)

from game_files.settings import *