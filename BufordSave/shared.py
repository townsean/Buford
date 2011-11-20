import os, pygame, math

def distance(x1,y1, x2,y2):
	return math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

def path(directory, filename):
	filePath = os.path.join(directory, filename) 
	return filePath
	
def loadImage(path, useColorKey = False, colorKeyPoint = (0,0)):
	image = pygame.image.load(path)
	image = image.convert()
	
	if useColorKey is True:
		colorkey = image.get_at(colorKeyPoint)
		image.set_colorkey(colorkey, pygame.RLEACCEL)
		
	return image
