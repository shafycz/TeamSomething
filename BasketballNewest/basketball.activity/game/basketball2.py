import spyral
import random

import math
#import wallbreaker
import test2
import game
import basketball



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"



class BasketBall2(spyral.Scene):

    def __init__(self):

        super(BasketBall2, self).__init__(SIZE)
	
	
        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        spyral.Scene.__init__(self, SIZE)
        if game.Color == 0:
        	self.background = spyral.Image(filename= "game/colors/blackb2.png")
        elif game.Color==1:
        	self.background = spyral.Image(filename= "game/colors/blueb2.png")
	if game.Color == 2:
        	self.background = spyral.Image(filename= "game/colors/greenb2.png")
        elif game.Color==3:
        	self.background = spyral.Image(filename= "game/colors/pinkb2.png")
	if game.Color == 4:
        	self.background = spyral.Image(filename= "game/colors/purpleb2.png")
        elif game.Color==5:
        	self.background = spyral.Image(filename= "game/colors/redb2.png")
	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",100,(255,255,255))
	#message = font.render("Click to Start");
	#StartMessage(self,message,(200),10)
   	#self.my1 = MyActor(self.c1)
	m2 = font.render(str(game.Counter))
	StartMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	StartMessage(self,m3,(1150),20)
    
    def handle_clicked(self, pos):
	if game.Balls >0:
		game.Counter = game.Counter +3
		game.Balls = game.Balls - 1
	elif game.Turns >0:
		game.Turns = game.Turns -1
		spyral.director.replace(basketball.Basketball())
	elif game.Counter > game.Counter1:
		print "YOU WIN"
	else:
		print "YOU LOSE"
	

 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






