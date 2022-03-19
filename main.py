import pygame, sys
import scenes, players
from pygame.locals import *
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it


def drawScreen(SCREEN, currentScene, player):
	'''This function draws everything to the SCREEN, which is  the game window'''
	SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
	
	#filling the scenes image with red, then drawing on the player
	currentScene.image.fill((255,0,0))
	pygame.draw.rect(currentScene.image, (0,255,0), (player.x, player.y, 20, 20))

	#drawing the scenes image onto the screen
	SCREEN.blit(currentScene.image, currentScene.rect)
	
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
	if keys[K_s]:
		player.y += player.speed
	if keys[K_a]:
		player.x -= player.speed
	if keys[K_d]:
		player.x += player.speed

def main():
	'''The main function for the game, calls all the others'''
	WIDTH, HEIGHT = 800, 600
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))#creating the game window
	pygame.display.set_caption('JameGam8')#naming the window

	FPS = 60
	CLOCK = pygame.time.Clock()

	#Setting up initial scene and player:
	currentScene = scenes.Scene('start', 500, 500)
	player = players.Player(100, 100, currentScene)

	while True:
		#This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
		gameLoop(currentScene, player)
		drawScreen(SCREEN, currentScene, player)
		CLOCK.tick(FPS)

		
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
	main()