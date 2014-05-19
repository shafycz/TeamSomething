import spyral
import random
import math
from spyral import Animation, easing
import time
import test
import game
import question
import mainMenu

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)




class Win(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
	if game.Win == True:
	
	  	self.background = spyral.Image(filename= "game/colors/winScreen.png")
	else:
		self.background = spyral.Image(filename= "game/colors/loseScreen.png")

   	
	spyral.event.register('input.keyboard.down.q', spyral.director.quit)
	

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register('input.keyboard.down.space', self.go_Next)
    
    def go_Next(self):
	spyral.director.pop
	spyral.director.replace(mainMenu.MainMenu())
