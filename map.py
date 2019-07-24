from pytmx.util_pygame import load_pygame
import pygame
import pyscroll
import pyscroll.data
import collections
import logging
from pygame.locals import *

import pyscroll.orthographic

# Game Initialization
pygame.init()
pygame.display.set_caption("Game")

# Game Resolution
screen_width = 1280
screen_height = 800

screen=pygame.display.set_mode((screen_width, screen_height))
 
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
 
# Game Fonts
dialogue_font = "fonts/Mohave-Italic.otf"
name_font = "fonts/Bebas.otf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

#Static Objects
textbox = pygame.image.load('images/textboxes/textbox_2.png').convert_alpha()
textbox = pygame.transform.scale(textbox, (screen_width, screen_height))