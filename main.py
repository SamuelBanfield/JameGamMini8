import pygame, sys
import scenes, players, ingredients, scenery
import interfaces
from pygame.locals import *
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it


def animate(entities):
    for i in range(len(entities)):
        entities[i].frame = entities[i].frame % entities[i].frames + 1
    
def drawScreen(SCREEN, currentScene, entities, bottleInterface):
    '''This function draws everything to the SCREEN, which is  the game window'''
    SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
    WIDTH, HEIGHT = SCREEN.get_size()

    #updating entity and scenery images then drawing them on
    currentScene.updateImage()
    currentScene.rect.center = (WIDTH//2, HEIGHT//2)
    for entity in entities:
        entity.updateImage()
        currentScene.image.blit(pygame.transform.scale(entity.image, entity.size),(entity.x,entity.y))
    
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

def main():
    '''The main function for the game, calls all the others'''
    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #creating the game window
    pygame.display.set_caption('JameGam8') #naming the window
    entities = [] #this should probably belong to the currentScene?

    FPS = 60
    CLOCK = pygame.time.Clock()

    #Setting up initial scene and player:
    currentScene = scenes.Scene('start', 500, 500)
    player = players.Entity(100, 100, 'Wizard', 'FaceDown', currentScene)

    currentScene.player = player
    currentScene.scenery.append(scenery.Scenery(100, 70, 'Door', currentScene, True))
    
    bottleInterface = interfaces.BottleInterface()

    entities.append(player)
    counter = 0

    while True:
        #This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
        counter += 1
        gameLoop(currentScene, player)
        drawScreen(SCREEN, currentScene, entities, bottleInterface)
        if counter % FPS == 0:
            animate(entities)
        CLOCK.tick(FPS)

        
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
    main()