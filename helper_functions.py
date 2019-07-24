import pygame
from pygame.locals import *

# Generate script list from txt file
def generate_script(file_path):
	with open(file_path, 'r') as f:
		lines = [line.strip() for line in f]
	cleaned_script = []
	for line in lines:
		components = line.split(':')
		name = components[0]
		message = components[1]
		cleaned_script.append((name, message))
	return cleaned_script

# Text renderer
def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, 0, textColor)
	return newText

# Generalized Event function (Not Working)
def event_queue(type=None):
	for event in pygame.event.get():
		if type is None:
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		elif type == 'display_text':
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x or event.key == pygame.K_z:
					skip = True
		elif type == 'next_dialogue':
			if event.type == QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x or event.key == pygame.K_z:
					return

