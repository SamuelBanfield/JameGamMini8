import pygame, scenery, boundaries
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
        self.entities = []
        self.boundaries = []
        self.collidableObjects = []

    def updateImage(self):
        img = self.image

        img.blit(backGround, backGroundRect)
        for obj in self.scenery:
            obj.updateImage()
            img.blit(obj.image, obj.rect)

    def update(self):
        p = self.player
        for entity in self.entities:
            if entity != p:
                #moving in the direction of the player
                if entity.x > p.x:
                    entity.move(-1,0)
                elif entity.x < p.x:
                    entity.move(1,0)
                if entity.y > p.y:
                    entity.move(0,-1)
                elif entity.y < p.y:
                    entity.move(0,1)

                #making the player face the right direction
                if (entity.x-p.x)**2 > (entity.y-p.y)**2:
                    if entity.x > p.x:
                        entity.caption = 'FaceLeft'
                    else:
                        entity.caption = 'FaceRight'
                else:
                    if entity.y > p.y:
                        entity.caption = 'FaceUp'
                    else:
                        entity.caption = 'FaceDown'

    def __str__(self):
        return self.name


def setup1(player):
    currentScene = Scene('start', 500, 500)

    player.scene = currentScene
    player.x, player.y = 100, 100
    currentScene.player = player
    currentScene.scenery.append(scenery.Scenery(225, 60, 'Door', scene=currentScene, animated=False, collidable=True))
    currentScene.scenery.append(scenery.Scenery(130, 60, 'Torch', scene=currentScene, animated=True))
    currentScene.scenery.append(scenery.Scenery(370, 60, 'Torch', scene=currentScene, animated=True))

    # Adds the map boundaries
    currentScene.collidableObjects.append(boundaries.Boundary(0, 80, 500, 30, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(0, 460, 500, 30, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(15, 0, 30, 500, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(450, 0, 30, 500, currentScene))

    currentScene.entities.append(player)

    return currentScene