import pygame
import os
import time
from helper_functions import *
#=====TEMPORARY=====

# Game Initialization
pygame.init()
pygame.display.set_caption("Game")

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width = 1280
screen_height = 800

screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, 0, textColor)
 
	return newText

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
 
# Game Fonts
menu_font = "fonts/mohave-italic.otf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

#=====TEMPORARY=====
def display_text(string):
	text = ''
	for i in range(len(string)):
		text += string[i]
		screen.fill(blue)
		screen.blit(textbox, (screen_width/2 - textbox_rect[2]/2, -10))
		text = text_format(text, menu_font, 75, white)
		text_rect = text.get_rect()
		screen.blit(text, (10, 10))
		pygame.display.update()
		pygame.tick(FPS)
		pygame.time.wait(1000)
		

def chap_1_1():
	textbox = pygame.image.load('textboxes/textbox_2.png').convert_alpha()
	textbox = pygame.transform.scale(textbox, (screen_width, screen_height))
	textbox_rect = textbox.get_rect()
	screen.fill(blue)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		screen.blit(textbox, (screen_width/2 - textbox_rect[2]/2, -10))
		# Update
		pygame.display.update()
		clock.tick(FPS)

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	chap_1_1()
	pygame.quit()
	quit()





