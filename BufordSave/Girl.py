import pygame
import shared
from pygame.sprite import *

class Girl(pygame.sprite.Sprite):
	""" Creates a sprite for the main character sprite """	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.font = pygame.font.SysFont("Verdana", 13)
		self.imageMaster = self.font.render(">girl>",
			True, (0,0,0), (0xFF, 0xFF, 0xFF))
		
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		
		self.x = 0
		self.y = 0
		self.rect.topleft = (self.x, self.y)
		self.width = 101
		self.height = 171

		self.pressed = False
		
		self.GOING_UP = 0
		self.GOING_DOWN = 1
		self.INACTIVE = 2
		self.DIE = 3
		self.SCARED = 4
		
		self.status = self.INACTIVE
		self.currentFrameIndex = 0
		self.frames = []
		
	def setImage(self, filename):
		filepath = shared.path("data", filename)
		image = shared.loadImage(filepath, True)
		self.frames = self.__generateGirlAnimation(image)
		currentFrame = 0
		self.imageFrame = self.__setCurrentFrame( currentFrame )

	def __setCurrentFrame(self, frame):
		if ( frame < len(self.frames) and (frame >= 0) ):
			self.imageMaster = self.frames[frame]

	def __generateGirlAnimation(self, image):
		""" Generates a set of surfaces to create a neeb growing animation """
		images = []
		master_image = image

		master_width, master_height = master_image.get_size()
		width = self.width
		height = self.height
		for index in range(int(master_width/width)):
			images.append(master_image.subsurface((index*width,0,width,height)))
			
		return images
		
	def setScared(self, isScared):
		if isScared:
			self.status = self.SCARED
		else:
			self.status = self.INACTIVE
			
	def update(self):
		if self.status == self.SCARED:
			self.__animateScared()
		else:
			self.__animateNormal()

		self.__setCurrentFrame(self.currentFrameIndex)
		
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x, self.y)
		
		self.CheckEvents()
		
	def __animateScared(self):
		self.currentFrameIndex = 1
	
	def __animateNormal(self):
		self.currentFrameIndex = 0
	
	def CheckEvents(self):
		self.mouseDown()
			
	def mouseDown(self):
		""" boolean function. Returns True if the mouse is 
			clicked over the sprite, False otherwise
		"""
		self.pressed = False
		if pygame.mouse.get_pressed() == (1, 0, 0):
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				print("MOUSE DOWN")
				self.pressed = True
		return self.pressed

	def clicked(self):
		""" Boolean function. Returns True only if mouse
			is pressed and released over sprite
		"""
		released = False
		if self.pressed:
			if pygame.mouse.get_pressed() == (0, 0, 0):
				if self.rect.collidepoint(pygame.mouse.get_pos()):
					print("CLICKED!")
					released = True
			return released

if __name__ == "__main__":
	import scene 
	from scene import Scene
	game = Scene()
	girl = Girl()
	game.sprites = [girl]
	girl.setImage("girl.png")
	game.start()
