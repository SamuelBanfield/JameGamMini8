import pygame
pygame.init()

imageDirectory = 'Art'
imagesDict = {'generic': pygame.image.load(imageDirectory+'/genericItem.png')}

class Ingredient:
	def __init__(self, name, x, y):
		self.name = name
		self.image = imagesDict[name]
		self.rect = self.image.get_rect()
		self.x, self.y = x, y
		self.rect.topleft = x, y

	def __str__(self):
		return self.name