import pygame
import os
import shared
import scene
import math

from os import *
from scene import Scene
from ChasingNeeb import ChasingNeeb
from Girl import Girl
from Buford import Buford
from Grass import Grass

class BufordSave(Scene):
	def __init__(self):
		Scene.__init__(self)
		self.screne = pygame.display.set_mode((450, 480))
		self.background.fill( (210,210,210) )
		
		background = Grass()
		self.girl = Girl()
		self.girl.setImage("girl.png")
		self.girl.x = 20
		self.girl.y = 25
		
		self.buford = Buford()
		self.buford.setImage("buford.gif")
		self.buford.x = self.girl.x + self.girl.width + 20
		self.buford.y = self.girl.y + self.girl.height + 28
		
		self.girl.setFollowingSprite(self.buford)
		
		self.sprites = [background, self.girl, self.buford]                               
		neebCount = 4
		self.neebSprites = []
		
		change= 50
		for x in range(neebCount):
			print("Making a neeb", change)
			self.neebSprites.append( ChasingNeeb() )
			self.neebSprites[x].setImage("neeb_still.gif")
			self.neebSprites[x].x = 0 + change
			self.neebSprites[x].y = 0
			self.sprites.append(self.neebSprites[x])
			change += 10
			
		self.neebGroup = Scene.makeSpriteGroup( self, self.neebSprites )
		
		#print( gameShared.distance(self.girl.x, self.girl.y, self.neebSprites[0].x, self.neebSprites[0].y) )
	
		self.girlScareDistance = 190
		self.neebScareDistance = 100
	
	def update(self):
		#print("UPDATING")
		isScared = False
		
		for neebSprite in self.neebSprites:
			# Handles the neeb walking towards the girl
			neebSprite.walkTimer+= 1
			if neebSprite.walkTimer >= neebSprite.walkSpeed_:
				neebSprite.walkTowardsGirl(self.girl)
				neebSprite.walkTimer = 0
			
			# Upadtes the girl if the neebs get too close
			if( self.isNeebNearGirl(neebSprite) ):
				isScared = True
			
			# Handles the case when buford gets close to a neeb
			isBufordClose = self.isNeebCloseToBufford(neebSprite)
			neebSprite.setIsBufordClose(isBufordClose)
			if isBufordClose:
				print("HE IS CLOSE!!!!")
				neebSprite.runAwayFromBuford(self.buford)
		
		#Update the girl if she is scared
		self.girl.setScared(isScared)
		
	def isNeebNearGirl(self, neeb):
		distance = shared.distance(self.girl.x, self.girl.y, neeb.x, neeb.y)
		#print("Current Distance: ", distance)
		return ( distance < self.girlScareDistance )
		
	def isNeebCloseToBufford(self, neeb):
		distance = shared.distance(self.buford.x, self.buford.y, neeb.x, neeb.y)
		return ( distance < self.neebScareDistance )

if __name__ == "__main__":
    game = BufordSave()
    game.start()
