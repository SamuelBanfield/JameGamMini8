import pygame

EntityCaptions = ['FaceDown','FaceUp','FaceLeft','FaceRight']
EntityTypes = ['Wizard']
Frames = 2
FrameDict = {}
for Etype in EntityTypes:
    for caption in EntityCaptions:
        for frame in range(1,Frames+1):
            FrameDict[Etype+caption+str(frame)] = pygame.image.load('Art/'+Etype+'/'+caption+str(frame)+'.png')

class Player:
    def __init__(self, x, y, Type, Caption, scene = None):
        self.x, self.y = x, y
        self.speed = 3
        self.scene = scene
        self.type = Type
        self.caption = Caption
        self.frame = 1
        self.frames = Frames
    
    def loadImg(self):
        self.Img = FrameDict[self.type+self.caption+str(self.frame)]