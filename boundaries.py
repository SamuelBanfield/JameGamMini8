import pygame

class Boundary:
    def __init__(self, x, y, width, height, scene):
        self.x, self.y = x, y
        self.scene = scene
        self.width, self.height = self.size = width, height
        scene.collidableObjects.append(self)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.size = (self.rect.width, self.rect.height)