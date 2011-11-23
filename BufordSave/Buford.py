import pygame
import shared
from pygame.sprite import *

class Buford(pygame.sprite.Sprite):
	""" Creates a Buford sprite """
		
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.font = pygame.font.SysFont("Verdana", 13)
		self.imageMaster = self.font.render(">Buford>",
			True, (0,0,0), (0xFF, 0xFF, 0xFF))
		
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		
		self.x = 200
		self.y = 200
		self.width = 33
		self.height = 66
		self.rect.topleft = (self.x, self.y)

		self.pressed = False
		
		#self.neebFrames = []		
		self.GOING_UP = 0
		self.GOING_DOWN = 1
		self.INACTIVE = 2
		self.DIE = 3
		
		self.status = self.INACTIVE
		self.currentFrameIndex = 0
		self.frames = []
		
	def setImage(self, filename):
		filepath = shared.path("data", filename)
		image = shared.loadImage(filepath, True)
		self.frames = self.__generateBufordAnimation(image)
		currentFrame = len(self.frames) - 1
		self.imageFrame = self.__setCurrentFrame( currentFrame )

	def __setCurrentFrame(self, frame):
		self.imageMaster = self.frames[frame]

	""" Generates a set of surfaces to create a neeb growing animation """
	def __generateBufordAnimation(self, image):
		images = []
		master_image = image

		master_width, master_height = master_image.get_size()
		width = self.width
		height = self.height
		for index in range(int(master_width/width)):
			images.append(master_image.subsurface((index*width,0,width,height)))

		print( len(images) )
		return images
			
	def update(self):
		#Where updating frames and changing animations 
		# can occur, as an example of below
		#if self.status == self.GOING_UP:
		#	self.__animateUp()
		#elif self.status == self.GOING_DOWN:
		#	self.__animateDown()
		#elif self.status == self.DIE:
		#	self.__animateKill()
			
		#self.__setCurrentFrame(self.currentFrameIndex)
		
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		self.rect.topleft = (self.x, self.y)
		
		#self.__updateAnimationState()
		
		self.CheckEvents()
	
	def CheckEvents(self):
		self.mouseDown()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.moveLeft()
		if keys[pygame.K_RIGHT]:
			self.moveRight()
		if keys[pygame.K_UP]:
			self.moveUp()
		if keys[pygame.K_DOWN]:
			self.moveDown()
			
	def mouseDown(self):
		""" boolean function. Returns True if the mouse is 
			clicked over the sprite, False otherwise
		"""
		#print("Check Mouse Down?")
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
		#print("CHECK CLICKED?!")
		released = False
		if self.pressed:
			if pygame.mouse.get_pressed() == (0, 0, 0):
				if self.rect.collidepoint(pygame.mouse.get_pos()):
					print("CLICKED!")
					released = True
			return released
			
	def moveLeft(self):
		self.x -= 5
		
	def moveRight(self):
		self.x += 5
		
	def moveUp(self):
		self.y -= 5
		
	def moveDown(self):
		self.y += 5

	def kill(self):
		self.isAnimationActive = False
		print("KILLED!")
		self.__animateKill()

	def __animateKill(self):
		print("ANIMATING DEATH")
		
	def __animateUp(self):
		#print("ANIMATING UP")
		print("CurrentIndex: ", self.currentFrameIndex, " TotalFrames:  ", len( self.frames ) )
		if (self.currentFrameIndex < len( self.frames ) - 1 ):
			self.currentFrameIndex += 1
			print("New Index", self.currentFrameIndex)
	
	def __animateDown(self):
		#print("ANIMATING DOwn")
		if (self.currentFrameIndex > 0 ):
			self.currentFrameIndex -=1
			
	def __updateAnimationState(self):
		#print("UPDATE ANIMATION STATE")
		if( self.currentFrameIndex == 0 ):
			self.status = self.INACTIVE
		elif( self.currentFrameIndex >= len( self.frames )-1 ):
			self.status = self.GOING_DOWN

	def popUp(self):
		print ("POP UP")
		self.status = self.GOING_UP
	
	def popDown(self):
		print ("POP DOWN")
		self.status = self.GOING_DOWN

if __name__ == "__main__":
	import scene 
	from scene import Scene
	from Girl import Girl
	game = Scene()
	buford = Buford()
	buford.setImage("buford.gif")
	girl = Girl()
	girl.setImage("girl.png");
	game.sprites = [buford, girl]
	game.start()
