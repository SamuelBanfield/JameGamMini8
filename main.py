import pygame, sys
import scenes, players, ingredients, scenery, interfaces, boundaries
from pygame.locals import *
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it

font20 = pygame.font.Font(pygame.font.get_default_font(), 20)

def animate(currentScene):
    for entity in currentScene.entities:
        entity.frame = entity.frame % entity.frames + 1
    for sceneryElement in currentScene.scenery:
        if sceneryElement.animated:
            sceneryElement.frame = sceneryElement.frame % sceneryElement.frames + 1
    
def drawScreen(SCREEN, currentScene, bottleInterface):
    '''This function draws everything to the SCREEN, which is  the game window'''
    SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
    WIDTH, HEIGHT = SCREEN.get_size()

    #updating entity and scenery images then drawing them on
    currentScene.updateImage()
    currentScene.rect.center = (WIDTH//2, HEIGHT//2)
    for entity in currentScene.entities:
        entity.updateImage()
        currentScene.image.blit(pygame.transform.scale(entity.image, entity.size),(entity.x,entity.y))

    if currentScene.player.contacts != []:
        for o in currentScene.player.contacts:
            if o.type == 'Door':
                fontImage = font20.render('Press f to enter door', True, (255,255,255))
                fontRect = fontImage.get_rect()
                w, h = currentScene.image.get_size()
                fontRect.center = (w//2, 5*h//6)
                currentScene.image.blit(fontImage, fontRect)
                break
    
    #drawing bottle interface, this is where ingredient mixing and stuff will happen
    bottleInterface.image.fill((200,200,200))
    bottleInterface.rect.center = WIDTH-bottleInterface.image.get_size()[0]//2, HEIGHT//2

    #drawing the interfaces onto the screen
    SCREEN.blit(currentScene.image, currentScene.rect)
    SCREEN.blit(bottleInterface.image, bottleInterface.rect)

    
    pygame.display.flip()#This function is called whenever we are finished drawing stuff to the screen, to make it display

def gameLoop(currentScene, player):
    '''This is the main game loop, where all the game logic will happen'''
    for event in pygame.event.get():
        #This loops handles all events, which is pretty much input from the user like clicks, keyboard presses and the mouse moving
        if event.type == QUIT:
            #This handles the user quitting the game by pressing x
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_f:
                if player.contacts != []:
                    for o in player.contacts:
                        if o.type == 'Door':
                            currentScene = scenes.setup1(player)
                            break


    #moving the player if the wasd keys are pressed:
    keys = pygame.key.get_pressed() #this returns a dictionary, and can be used to check whether different keys are pressed
    if keys[K_w] or keys[K_UP]:
        player.move(0, -player.speed)
        player.caption = 'FaceUp'
    if keys[K_s] or keys[K_DOWN]:
        player.move(0, player.speed)
        player.caption = 'FaceDown'
    if keys[K_a] or keys[K_LEFT]:
        player.move(-player.speed, 0)        
        player.caption = 'FaceLeft'
    if keys[K_d] or keys[K_RIGHT]:
        player.move(player.speed, 0)
        player.caption = 'FaceRight'
    currentScene.update()
    return currentScene

def main():
    '''The main function for the game, calls all the others'''
    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #creating the game window
    pygame.display.set_caption('JameGam8') #naming the window

    FPS = 60
    CLOCK = pygame.time.Clock()

    #Setting up initial scene and player:
    currentScene = scenes.Scene('start', 500, 500)
    player = players.Player(100, 100, 'Wizard', 'FaceDown', currentScene, pygame.Rect(0,0,16,10),[8,15])
    player.collisionRect = pygame.Rect((player.x, player.y, player.width//2, player.height//2))

    # Adds objects to the current scene
    currentScene.player = player
    currentScene.scenery.append(scenery.Scenery(225, 60, 'Door', scene=currentScene, animated=False, collidable=True))
    currentScene.scenery.append(scenery.Scenery(130, 60, 'Torch', scene=currentScene, animated=True))
    currentScene.scenery.append(scenery.Scenery(370, 60, 'Torch', scene=currentScene, animated=True))
    
    currentScene.entities.append(players.Entity(100, 200, 'Skeleton', 'FaceDown', scene = currentScene, collisionRect = None, offset = [0,0]))

    # Adds the map boundaries
    currentScene.collidableObjects.append(boundaries.Boundary(0, 80, 500, 30, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(0, 460, 500, 30, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(15, 0, 30, 500, currentScene))
    currentScene.collidableObjects.append(boundaries.Boundary(450, 0, 30, 500, currentScene))
    
    bottleInterface = interfaces.BottleInterface()

    #Adds entities to the current scene
    currentScene.entities.append(player)
    
    counter = 0

    while True:
        #This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
        counter += 1
        currentScene = gameLoop(currentScene, player)
        drawScreen(SCREEN, currentScene, bottleInterface)
        if counter % FPS == 0:
            animate(currentScene)
        CLOCK.tick(FPS)

        
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
    main()