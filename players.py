import pygame

class Player:
    def __init__(self, x, y, Type, Caption, scene = None):
        self.x, self.y = x, y
        self.speed = 3
        self.scene = scene
        self.type = Type
        self.caption = Caption
        self.frame = 1
        self.frames = 2
        
    def load(self):
        self.Img = pygame.image.load('Art/'+self.type+'/'+self.caption+str(self.frame)+'.png')