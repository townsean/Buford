'''
Created on Sep 25, 2011

@author: SeriousHornCat
'''

import pygame, os
from pygame.locals import *

class Scene(object):
    '''
    A base class used for creating mini games.  Source code from
	'Game Programming' by Andy Harris.
    '''

    def __init__(self):
        '''
        Initializes a Scene for the game
        '''
        pygame.init()
        self.screen = pygame.display.set_mode( (640, 480) )
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill( (0,0,0) )
        
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        self.sprites = []
        self.groups = []

        self.isRunning = False
        
    def start(self):
        '''
        Starts the scene within begins the game loop
        '''
        self.mainSprites = pygame.sprite.LayeredUpdates(self.sprites)
        self.groups.insert(1, self.mainSprites)
        
        self.screen.blit(self.background, (0,0))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        
        while self.isRunning:
            self.__mainLoop()
            
    def stop(self):
        self.running = False

    def isRunning(self):
        return self.running

    def forceQuit(self):
        pygame.quit()

    def __mainLoop(self):
        self.clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            self.doEvents(event)
        
        self.update()
        #print( len(self.groups) )
        for group in self.groups:
            #group.clear(self.screen, self.background)
            group.update()
            group.draw(self.screen)
            
        pygame.display.flip()
        
    def makeSpriteGroup(self, sprites):
        tempGroup = pygame.sprite.LayeredUpdates(sprites)
        return tempGroup
    
    def makeDirtySpriteGroup(self, sprites):
        tempGroup = pygame.sprite.LayeredDirty(sprites)
        return tempGroup
    
    def addGroup(self, group):
        self.groups.append(group)
    
    def doEvents(self, event):
        '''
        This method is meant to be overloaded in inherited scenes.
        This method is add events unique to the scene
        '''
        pass
    
    def update(self):
        '''
        This occurs once per frame.  
        Example: Event handling that doesn't require an event object
        or possible collision detection.
        '''
        pass
    
    def setWindowTitle(self, title):
        pygame.display.set_caption(title)
        
if __name__ == "__main__":
    gameEngine = Scene()
    
    gameEngine.start()
    
