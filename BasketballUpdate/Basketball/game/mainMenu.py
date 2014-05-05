import spyral
import random

import math
import basketball
import game



WIDTH = 1200

HEIGHT = 900
BG_COLOR = (0,0,0)

WHITE = (255, 255, 255)

SIZE = (WIDTH, HEIGHT)

DEF_FONT = "libraries/spyral/resources/fonts/DejaVuSans.ttf"


class MainMenu(spyral.Scene):

    def __init__(self):

        super(MainMenu, self).__init__(SIZE)


        spyral.event.register('input.keyboard.down.q', spyral.director.quit)

        spyral.event.register("system.quit", spyral.director.quit)
	spyral.event.register("input.mouse.down.left", self.handle_clicked) 

        self.background = spyral.Image(filename= "game/background1.png")
	#self.start = Start(self,600,300)
	
	font = spyral.Font("/usr/share/fonts/truetype/freefont/FreeMono.ttf",60,(255,255,255))
	m1 = font.render("Basketball Grammar");
	StartMessage(self,m1,(200),10)
	m2 = font.render(str(game.Counter))
	StartMessage(self,m2,(960),20)
	m3 = font.render(str(game.Counter1))
	StartMessage(self,m3,(1150),20)
	
   
    def handle_clicked(self, pos):
	   	
	if pos.y <450:
		
		print game.Counter		
		game.Counter = game.Counter +1
		print game.Counter
		spyral.director.push(basketball.Basketball())
class StartMessage(spyral.Sprite):
	def __init__(self,scene,img,x,y):
		spyral.Sprite.__init__(self,scene)
		self.image = img
		self.x = x
		self.y = y






