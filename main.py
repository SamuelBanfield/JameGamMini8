import pygame, sys
import scenes, players
from pygame.locals import *
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it

def animate(Entities):
    for i in range(len(Entities)):
        Entities[i].frame = Entities[i].frame % Entities[i].frames + 1
    
def drawScreen(SCREEN, currentScene, player):
    '''This function draws everything to the SCREEN, which is  the game window'''
    SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
    
    #filling the scenes image with red, then drawing on the player
    currentScene.image.fill((200,200,200))
    # pygame.draw.rect(currentScene.image, (0,255,0), (player.x, player.y, 20, 20))
    
    #drawing the scenes image onto the screen
    SCREEN.blit(currentScene.image, currentScene.rect)
    SCREEN.blit(pygame.transform.scale(player.Img, (150,150)),(player.x,player.y))
    
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
    if keys[K_w]:
        player.y -= player.speed
        player.caption = 'FaceUp'
    if keys[K_s]:
        player.y += player.speed
        player.caption = 'FaceDown'
    if keys[K_a]:
        player.x -= player.speed
        player.caption = 'FaceLeft'
    if keys[K_d]:
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
    player = players.Player(100, 100, 'Wizard', 'FaceDown', currentScene)
    
    Entities = [player]
    counter = 0
    while True:
        #This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
        counter += 1
        gameLoop(currentScene, player)
        player.load()
        drawScreen(SCREEN, currentScene, player)
        if counter % (FPS/2) == 0:
            animate(Entities)
        CLOCK.tick(FPS)

        
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
    main()