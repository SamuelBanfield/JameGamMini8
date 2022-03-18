import pygame, sys
pygame.init()
#importing pygame, pygame.init() just loads some python stuff, you can ignore it


def drawScreen(SCREEN):
	'''This function draws everything to the SCREEN, which is  the game window'''
	SCREEN.fill((0,0,0)) #fills the screen in black, otherwise whatever we drew last time will still be there
	pygame.draw.rect(SCREEN, (255,0,0), (50,50,100,100)) #drawing a rectangle, just as an example
	pygame.display.flip()#This function is called whenever we are finished drawing stuff to the screen, to make it display

def gameLoop():
	'''This is the main game loop, where all the game logic will happen'''
	for event in pygame.event.get():
		#This loops handles all events, which is pretty much input from the user like clicks, keyboard presses and the mouse moving
		if event.type == pygame.QUIT:
			#This handles the user quitting the game by pressing x 
			pygame.quit()
			sys.exit()

def main():
	'''The main function for the game, calls all the others'''
	WIDTH, HEIGHT = 800, 600
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))#creating the game window
	pygame.display.set_caption('JameGam8')#naming the window

	FPS = 60
	CLOCK = pygame.time.Clock()

	while True:
		#This loop happens FPS times a second and calls all the core functions, getting input from the user, doing the game logic and drawing the screen
		gameLoop()
		drawScreen(SCREEN)
		CLOCK.tick(FPS)

		
#You can ignore this, all it does is call the main function when you run the program
if __name__ == "__main__":
	main()