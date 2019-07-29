import pygame
from pygame.locals import *
import os
from story import *
# Game Initialization
pygame.init()
pygame.display.set_caption("Game")

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
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
menu_font = "fonts/mohave-italic.otf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30
# Main Menu

# Images
file_paths = []
for file in os.listdir('vector_frames'):
	if file.endswith('.png'):
		file_paths.append('vector_frames/' + file)
file_paths.sort()
images = []
for path in file_paths:
	img = pygame.image.load(path).convert_alpha()
	img = pygame.transform.scale(img, (80, 80))
	images.append(img)

image_rect = images[0].get_rect()

def main_menu():
	current_frame = 0
	while True:
		screen.fill(gray)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		screen.blit(images[current_frame], (10, 10))
		current_frame += 1
		if current_frame == len(images):
			current_frame = 0
		# Update
		pygame.display.update()
		clock.tick(FPS)

def begin_game():
	return None

# Main Game Loop
crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	main_menu()
	pygame.quit()
	quit()