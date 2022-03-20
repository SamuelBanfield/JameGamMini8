import pygame

# SceneryStates = ['Closed']
SceneryTypes = ['Door']
imageDict = {}
for Stype in SceneryTypes:
    imageDict[Stype] = pygame.image.load('Art/Scenery/'+Stype+'.png')

class Scenery:
    def __init__(self, x, y, Type, scene = None):
        self.x, self.y = x, y
        self.type = Type
        
    def updateImage(self):
        self.Img = imageDict[self.type]
        