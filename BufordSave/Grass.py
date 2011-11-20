import pygame
import shared
from pygame.sprite import *

class Grass(pygame.sprite.Sprite):
	""" Creates a Buford sprite """
		
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		filenamepath = shared.path("data", "background.gif")
		self.image = shared.loadImage(filenamepath)
		self.image.convert()
		self.rect = self.image.get_rect()
		self.dy = 2
		self.rect.topleft = (0,0)
		self.maxHeight = 640
		self.reset()
		
	def update(self):
		self.rect.bottom += self.dy
		if self.rect.top >= 0:
			self.reset()
	
	def reset(self):
		self.rect.bottom = self.maxHeight
		
def main():
	import scene
	from scene import Scene
	game = Scene()
	grassBackground = Grass()
	game.sprites = [grassBackground]
	game.start()

if __name__ == "__main__":
	main()
