import pygame
from pygame.locals import *

def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, 0, textColor)
 
	return newText

def display_text_animation(screen, string):
	text = ''
	for i in range(len(string)):
		text += string[i]
		text_surface = text_format(text, 'Bebas.otf', 75, (0,0,0))
		text_rect = text_surface.get_rect()
		text_rect.center = (100, 100)
		screen.blit(text_surface, text_rect)
		pygame.display.update()
		pygame.time.wait(100)