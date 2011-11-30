import pygame
from pygame.sprite import *
from ChasingNeeb import ChasingNeeb

class NeebDepot(object):
	"""Container for holding all of the neebs"""
	
	def __init__(self, gameSize):
		self.neebSprites_ = []
		self.neebGroup_ = pygame.sprite.Group( self.neebSprites_ )
		self.gameSize_	= gameSize
		
	def neebSprites(self):
		return self.neebSprites_
		
	def generateSprites(self, amount):
		print("Generate Sprites")
		change = 50
		for x in range(amount):
			self.neebSprites_.append( ChasingNeeb() )
			self.neebSprites_[x].setImage("neeb_still.gif")
			self.neebSprites_[x].x = 0 + change
			self.neebSprites_[x].y = 0
			change += 10
			
		self.neebGroup_ = pygame.sprite.Group( self.neebSprites_ )
		print("DONE")
		
			
	def checkCollision(self):
		print("COLLIISION")
		print("AGAIN")
		for neeb in self.neebSprites_:
			collidedNeeb = pygame.sprite.spritecollideany(neeb, self.neebGroup_)
			if collidedNeeb is not None:
				
				neeb.x += collidedNeeb.width
				neeb.y += collidedNeeb.height
				print("New Neeb Location (", neeb.x,",", neeb.y,")" )
		
if __name__ == "__main__":
	import scene 
	from scene import Scene

	game = Scene()
	neebs = NeebDepot()
	neebs.generateSprites(5)
	game.sprites = [ neebs.neebSprites() ]
	for x in range(5):
		neebs.checkCollision()
	game.start()
	