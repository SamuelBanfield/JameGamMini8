import pygame

EntityCaptions = ['FaceDown','FaceUp','FaceLeft','FaceRight']
EntityTypes = ['Wizard']
Frames = 2
FrameDict = {}
for Etype in EntityTypes:
    for caption in EntityCaptions:
        for frame in range(1,Frames+1):
            FrameDict[Etype+caption+str(frame)] = pygame.image.load('Art/'+Etype+'/'+caption+str(frame)+'.png')

class Entity:
    def __init__(self, x, y, Type, Caption, scene = None):
        self.x, self.y = x, y
        self.speed = 3
        self.scene = scene
        self.type = Type
        self.caption = Caption
        self.frame = 1
        self.frames = Frames

    def move(self, xmovement, ymovement):
        #Entities must be attached to scenes, or this throws an error
        oldx, oldy = self.x, self.y
        newx = oldx+xmovement
        newy = oldy+ymovement
        #first handling collisions in x direction:
        for obj in self.scene.collidableObjects:
            if inside(newx, oldy, self.width, self.height, obj.rect):
                if oldx<=obj.rect.left:
                    newx = obj.rect.left-self.width
                else:
                    newx = obj.rect.right

        #then handling collisions in y direction:
        for obj in self.scene.collidableObjects:
            if inside(newx, newy, self.width, self.height, obj.rect):
                if oldy<=obj.rect.top:
                    newy = obj.rect.top-self.height
                else:
                    newy = obj.rect.bottom
        self.x, self.y = newx, newy
            
    def updateImage(self):
        self.image = FrameDict[self.type+self.caption+str(self.frame)]
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.width, self.rect.height
        self.size = (self.width, self.height)

def inside(x, y, width, height, rect):
    return rect.top-height<y<rect.bottom and rect.left-width<x<rect.right