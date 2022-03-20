import pygame

# SceneryStates = ['Closed']
SceneryTypes = ['Door']
imageDict = {}
for Stype in SceneryTypes:
    imageDict[Stype] = pygame.image.load('Art/Scenery/'+Stype+'.png')

class Scenery:
    def __init__(self, x, y, typeOf, scene = None, collidable = False):
        self.x, self.y = x, y
        self.type = typeOf
        self.scene = scene
        self.collidable = collidable
        if self.collidable:
            if scene == None:
                print('AAAAA, collidable object not attached to a scene')
            else:
                scene.collidableObjects.append(self)
        self.updateImage()
        
    def updateImage(self):
        self.image = imageDict[self.type]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.size = (self.rect.width, self.rect.height)

        