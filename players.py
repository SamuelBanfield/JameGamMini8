import pygame

entityCaptions = ['FaceDown','FaceUp','FaceLeft','FaceRight']
entityTypes = ['Wizard']
Frames = 2
FrameDict = {}
for Etype in entityTypes:
    for caption in entityCaptions:
        for frame in range(1,Frames+1):
            FrameDict[Etype+caption+str(frame)] = pygame.image.load('Art/'+Etype+'/'+caption+str(frame)+'.png')

class Entity:
    def __init__(self, x, y, Type, Caption, scene = None, collisionRect = None, offset = [0,0]):
        self.x, self.y = x, y
        self.speed = 3
        self.scene = scene
        self.type = Type
        self.caption = Caption
        self.frame = 1
        self.frames = Frames
        self.updateImage()

        #setting up collision rect, if no collision rect and offset are provided, collisionRect defaults to being image rect
        self.offset = offset
        if collisionRect == None:
            self.collisionRect = self.rect
        else:
            self.collisionRect = collisionRect
            self.collisionRect.topleft = self.x+self.offset[0], self.y+self.offset[1]
            print(self.collisionRect)

    def move(self, xmovement, ymovement):
        '''This function checks a desired movement to see if it causes collisions, and changes the movement appropriately'''
        
        #Entities must be attached to scenes, or this throws an error
        oldx, oldy = self.x+self.offset[0], self.y+self.offset[1]
        newx, newy= oldx+xmovement, oldy+ymovement

        w, h = self.collisionRect.width, self.collisionRect.height
        #first handling collisions in x direction:
        for obj in self.scene.collidableObjects:
            if inside(newx, oldy, w, h, obj.rect):
                if oldx<=obj.rect.left:
                    newx = obj.rect.left-w
                else:
                    newx = obj.rect.right

        #then handling collisions in y direction:
        for obj in self.scene.collidableObjects:
            if inside(newx, newy, w, h, obj.rect):
                if oldy<=obj.rect.top:
                    newy = obj.rect.top-h
                else:
                    newy = obj.rect.bottom
        self.x, self.y = newx-self.offset[0], newy-self.offset[1]
            
    def updateImage(self):
        self.image = FrameDict[self.type+self.caption+str(self.frame)]
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.width, self.rect.height
        self.size = (self.width, self.height)

def inside(x, y, width, height, rect):
    return rect.top-height<y<rect.bottom and rect.left-width<x<rect.right