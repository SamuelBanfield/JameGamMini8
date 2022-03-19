import pygame, sys
import scenes, players, ingredients
import interfaces
from pygame.locals import *
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it

"""This looks very cool joe, one thing is it loads the images every time, which will get slow, so it might be better to load all the images into an image dict, then use 'caption' to select current image from the image dict raher than choosing which one to load"""
#ive addded map objects, im not sure if you were aniticipating them being the same as 'entities', but i assumed it would be for enemies and stuff


def animate(Entities):
    for i in range(len(Entities)):
        Entities[i].frame = Entities[i].frame % Entities[i].frames + 1
    
def drawScreen(SCREEN, currentScene, player, bottleInterface):
    '''This function draws everything to the SCREEN, which is  the game window'''
    SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
    WIDTH, HEIGHT = SCREEN.get_size()

    #filling the scenes image with red, then drawing on the player
    currentScene.updateImage()
    currentScene.rect.center = (WIDTH//2, HEIGHT//2)
    currentScene.image.blit(pygame.transform.scale(player.Img, (150,150)),(player.x,player.y))
    
    #drawing bottle interface, this is where ingredient mixing and stuff will happen?
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
        player.y -= player.speed
        player.caption = 'FaceUp'
    if keys[K_s] or keys[K_DOWN]:
        player.y += player.speed
        player.caption = 'FaceDown'
    if keys[K_a] or keys[K_LEFT]:
        player.x -= player.speed
        player.caption = 'FaceLeft'
    if keys[K_d] or keys[K_RIGHT]:
        player.x += player.speed
        player.caption = 'FaceRight'

def main():
    '''The main function for the game, calls all the others'''
    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))#creating the game window
    pygame.display.set_caption('JameGam8')#naming the window

    FPS = 60
    CLOCK = pygame.time.Clock()

    #Setting up initial scene and player:
    currentScene = scenes.Scene('start', 500, 500)
    currentScene.mapObjects.append(ingredients.Ingredient('generic', 20, 20))
    player = players.Player(100, 100, 'Wizard', 'FaceDown', currentScene)
    
    bottleInterface = interfaces.BottleInterface()

    Entities = [player]

    counter = 0

    while True:
        #This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
        counter += 1
        gameLoop(currentScene, player)
        player.loadImg()
        drawScreen(SCREEN, currentScene, player, bottleInterface)
        if counter % FPS == 0:
            animate(Entities)
        CLOCK.tick(FPS)

        
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
    main()