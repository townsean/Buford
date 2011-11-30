import pygame
import shared
from pygame.sprite import *

class ChasingNeeb(pygame.sprite.Sprite):
	""" Creates a ChasingNeeb sprite """
		
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.font = pygame.font.SysFont("Verdana", 13)
		self.imageMaster = self.font.render(":3",
			True, (0,0,0), (0xFF, 0xFF, 0xFF))
		
		self.image = self.imageMaster
		self.rect = self.image.get_rect()
		
		self.x = 0
		self.y = 0
		self.width = 75
		self.height = 43
		self.rect.topleft = (self.x, self.y)

		self.pressed = False
		
		#self.neebFrames = []		
		self.GOING_UP = 0
		self.GOING_DOWN = 1
		self.INACTIVE = 2
		self.DIE = 3
		self.WALKING = 4
		self.RUN_AWAY_FROM_BUFORD = 5
		
		self.status = self.INACTIVE
		self.currentFrameIndex = 0
		self.frames = []
		
		#Number represents amount of frames to puase for walking
		self.WALK_FAST = 7
		self.WALK_REGULAR = 15
		self.WALK_SLOW = 25
		
		self.walkSpeed_= self.WALK_FAST
		self.walkTimer = 0
		
	def setWalkFast(self):
		self.walkSpeed_ = self.WALK_FAST
		
	def setWalkRegular(self):
		self.walkSpeed_ = self.WALK_REGULAR
		
	def setWalkSlow(self):
		self.walkSpeed_ = self.WALK_SLOW
	
	def setImage(self, filename):
		filepath = shared.path("data", filename)
		image = shared.loadImage(filepath, True)
		self.frames = self.__generateNeebAnimation(image)
		currentFrame = len(self.frames) - 1
		self.imageFrame = self.__setCurrentFrame( currentFrame )

	def __setCurrentFrame(self, frame):
		self.imageMaster = self.frames[frame]
		
	def setIsBufordClose(self, isClose):
		if isClose:
			self.status = self.RUN_AWAY_FROM_BUFORD
		else:
			self.status = self.WALKING

	def walkTowardsGirl(self, girl):
		if ( self.status == self.WALKING ):
			print("RUN TOWARDS!")
			if (self.isCharacterAbove(girl.y)):
				self.y -= 5
			elif(self.isCharacterBelow(girl.y)):
				self.y += 5
				
			if(self.isCharacterLeft(girl.x)):
				self.x -=5
			elif(self.isCharacterRight(girl.x)):
				self.x +=5
			
	def runAwayFromBuford(self, buford):
		if (self.status == self.RUN_AWAY_FROM_BUFORD):
			print("RUN AWAYYYY!")
			if (self.isCharacterAbove(buford.y)):
				self.y += 10
			elif(self.isCharacterBelow(buford.y)):
				self.y -= 10
			if(self.isCharacterLeft(buford.x)):
				self.x -= 10
			elif(self.isCharacterRight(buford.x)):
				self.x += 10
	
	def isCharacterAbove(self, girlY):
		return ( girlY < self.y )
		
	def isCharacterBelow(self, girlY):
		return ( girlY > self.y )
		
	def isCharacterLeft(self, girlX):
		return ( girlX < self.x )
		
	def isCharacterRight(self, girlX):
		return ( girlX > self.x )

	""" Generates a set of surfaces to create a neeb growing animation """
	def __generateNeebAnimation(self, image):
		images = []
		master_image = image

		master_width, master_height = master_image.get_size()
		width = self.width
		height = self.height
		for index in range(int(master_width/width)):
			images.append(master_image.subsurface((index*width,0,width,height)))

		#print( len(images) )
		return images
			
	def update(self):
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
		
		#keys = pygame.key.get_pressed()
		#if keys[pygame.K_LEFT]:
		#	self.moveLeft()
		#if keys[pygame.K_RIGHT]:
		#	self.moveRight()
		#if keys[pygame.K_UP]:
		#	self.moveUp()
		#if keys[pygame.K_DOWN]:
		#	self.moveDown()
			
	def moveLeft(self):
		self.x -= 5
		
	def moveRight(self):
		self.x += 5
		
	def moveUp(self):
		self.y -= 5
		
	def moveDown(self):
		self.y += 5
			
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
	from Buford import Buford
	game = Scene()
	buford = Buford()
	buford.setImage("buford.gif")
	girl = Girl()
	girl.setImage("girl.png")
	chasingNeeb = ChasingNeeb()
	chasingNeeb.setImage("neeb_still.gif")
	game.sprites = [buford, girl, chasingNeeb]
	game.start()
