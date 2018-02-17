#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) #assigns a tuple variable to be 800 by 600, presumably the resolution in pixels
FPS = 60 #assigns an integer variable to be "FPS", presumably the number of frames rendered per second

def main(): #the main function of the program
	pygame.init() #Starts pygame
	screen = pygame.display.set_mode(screen_size) #creates a screen variable to be the pygame function display set mode which takes a tuple and makes a window
	clock = pygame.time.Clock() #Initializes a clock variable

	while True: #main game loop continues forever
		clock.tick(FPS) #waits 1/60 of a second 
		screen.fill((0,0,0)) #Fills screen with color (0, 0, 0)

		for event in pygame.event.get(): #if pygame gets an event
			if event.type == pygame.QUIT: #if that event is quit
				pygame.quit() #quits the game
				sys.exit(0) #also end the program

		pygame.display.flip() #flip renders all pixels at once

if __name__ == '__main__': #if run externally:
	main() #run the program
