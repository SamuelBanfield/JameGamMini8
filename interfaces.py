import pygame

class BottleInterface():
	def __init__(self):
		self.image = pygame.Surface((100,400))
		self.rect = self.image.get_rect()