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
menu_font = "Bebas.otf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

#Static Objects
textbox = pygame.image.load('textboxes/textbox_2.png').convert_alpha()
textbox = pygame.transform.scale(textbox, (screen_width, screen_height))

#=====TEMPORARY=====

def setup():
	global textbox
	textbox_rect = textbox.get_rect()
	screen.fill(blue)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	screen.blit(textbox, (screen_width/2 - textbox_rect[2]/2, -10))
	# Update
	pygame.display.update()
	clock.tick(FPS)

def display_text(name, string):
	global textbox
	textbox_rect = textbox.get_rect()
	text = ''
	skip = False
	for i in range(len(string)):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x or event.key == pygame.K_z:
					skip = True
		if skip:
			screen.fill(blue)
			screen.blit(textbox, (screen_width/2 - textbox_rect[2]/2, -10))
			formatted_text = text_format(string, menu_font, 75, white)
			formatted_name = text_format(name, menu_font, 30, white)
			text_rect = formatted_text.get_rect()
			name_rect = formatted_name.get_rect()
			screen.blit(formatted_text, (180, screen_height - 150))
			screen.blit(formatted_name, (120, screen_height - 200))
			pygame.display.update()
			break
		text += string[i]
		screen.fill(blue)
		screen.blit(textbox, (screen_width/2 - textbox_rect[2]/2, -10))
		formatted_text = text_format(text, menu_font, 75, white)
		formatted_name = text_format(name, menu_font, 30, white)
		text_rect = formatted_text.get_rect()
		name_rect = formatted_name.get_rect()
		screen.blit(formatted_text, (180, screen_height - 150))
		screen.blit(formatted_name, (120, screen_height - 200))
		pygame.display.update()
		pygame.time.wait(100)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x or event.key == pygame.K_z:
					return

script = [('Kevin', 'hi.....................'), ('James', 'hello.....................'), ('', 'no name! spooky!')]
def main():
	setup()
	for line in script:
		display_text(line[0], line[1])
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()
main()

