import pygame

class Scene:
	def __init__(self, name, width, height):
		self.name = name
		self.image = pygame.Surface((width, height)) #This is an image to which stuff on the screen can be drawn
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect() #pygame rect object gives a location to draw the scene image, used when drawing the image to the screen
		self.width, self.height = width, height
		self.mapObjects = [] #to store the location of random map objects and stuff

	def updateImage(self):
	    img = self.image

	    img.fill((200,200,200))
	    for obj in self.mapObjects:
	    	img.blit(obj.image, obj.rect)

	def __str__(self):
		return self.name