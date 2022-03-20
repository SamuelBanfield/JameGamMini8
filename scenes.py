import pygame
pygame.init()

backGround = pygame.image.load('Art/Scenery/Backgrounds/Room1.png')
backGroundRect = backGround.get_rect()

class Scene:
    def __init__(self, name, width, height, player = None):
        self.player = player
        self.name = name
        self.image = pygame.Surface((width, height)) #This is an image to which stuff on the screen can be drawn
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect() #pygame rect object gives a location to draw the scene image, used when drawing the image to the screen
        self.width, self.height = width, height
        self.scenery = [] #to store the location of random map objects and stuff
        self.entities = [] #stores the entities
        self.collidableObjects = []

    def updateImage(self):
        img = self.image

        img.blit(backGround, backGroundRect)
        for obj in self.scenery:
            obj.updateImage()
            img.blit(obj.image, obj.rect)

    def __str__(self):
        return self.name