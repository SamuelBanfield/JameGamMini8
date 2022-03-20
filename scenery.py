import pygame

# sceneryStates = ['Closed']
sceneryTypes = ['Door', 'Torch']
sceneryAnimated = [False, True]
sceneryFrames = ['1','2']
imageDict = {}
for i, stype in enumerate(sceneryTypes):
    if sceneryAnimated[i]:
        for frame in sceneryFrames:
            imageDict[stype+frame] = pygame.image.load('Art/Scenery/'+stype+frame+'.png')
    else:
        imageDict[stype] = pygame.image.load('Art/Scenery/'+stype+'.png')

class Scenery:
    def __init__(self, x, y, typeOf, scene = None, animated = False, collidable = False):
        self.x, self.y = x, y
        self.type = typeOf
        self.scene = scene
        self.collidable = collidable
        self.animated = animated
        if self.animated:
            self.frame = 1
            self.frames = len(sceneryFrames)
        if self.collidable:
            if scene == None:
                print('AAAAA, collidable object not attached to a scene')
            else:
                scene.collidableObjects.append(self)
        self.updateImage()
        
    def updateImage(self):
        if self.animated:
            self.image = imageDict[self.type+str(self.frame)]
        else:
            self.image = imageDict[self.type]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.size = (self.rect.width, self.rect.height)

        