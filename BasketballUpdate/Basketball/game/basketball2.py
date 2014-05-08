import spyral
import random

import math
#import wallbreaker
import test2
import game
import basketball
from spyral import Animation, easing


WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"

class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__(scene)
        
    	self.image = spyral.Image("game/1.png")
	self.anchor = 'center'
	self.pos = (WIDTH-1100, HEIGHT-50)

class BasketBall2(spyral.Scene):

    def __init__(self):

        super(BasketBall2, self).__init__(SIZE)
	
	self.ball = Ball(self)
        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 
	#spyral.event.register("input.mouse.down.space", self.jumpBlockButton)
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
    
    def handle_clicked():
	if game.Balls >0:
		game.Counter = game.Counter +3
		game.Balls = game.Balls - 1
		print "I'm clicking"		
		self.ball.animate(anim)
		#self.ball.animate(missAnim)
	elif game.Turns >0:
		game.Turns = game.Turns -1
		spyral.director.replace(basketball.Basketball())
	elif game.Counter > game.Counter1:
		print "YOU WIN"
	else:
		print "YOU LOSE"
	

	



	


	#if the player makes it -- the only option right now
	xCoordAnim = Animation('x', easing.Linear(WIDTH-1100, WIDTH-100), duration = 5.0)
	yCoordAnim1 = Animation('y', easing.QuadraticOut(HEIGHT-50, HEIGHT-750),duration=3.75)
	yCoordAnim2 = Animation('y', easing.QuadraticIn(HEIGHT-750,HEIGHT-50), duration = 1.25)
	
	anim = xCoordAnim & (yCoordAnim1 + yCoordAnim2)


##	#if the player misses it -- Commented out because I'm not sure what we're doing about missing freethrows but here's an example for future reference
	#missAnimX1 = Animation('x', easing.Linear(WIDTH-1100, WIDTH-200), duration = 4.5)
	#missAnimX2 = Animation('x', easing.Linear(WIDTH-200, WIDTH-600), duration = 0.1)
	#missAnimY1 = Animation('y', easing.QuadraticOut(HEIGHT-50, HEIGHT-750),duration=3.75)
	#missAnimY2 = Animation('y', easing.QuadraticIn(HEIGHT-750,HEIGHT-550), duration = 0.75)
	#missAnimY3 = Animation('y', easing.Linear(HEIGHT-550,HEIGHT-950), duration = 0.1)
		
	
	#missAnim = (missAnimX1 & (missAnimY1 + missAnimY2)) + (missAnimX2 & missAnimY3)






 
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






